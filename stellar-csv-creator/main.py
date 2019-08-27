import csv
import json
import logging
import sys
from datetime import datetime

import requests
import requests_cache
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql

from gui.about import Ui_Dialog
from gui.main_window import Ui_MainWindow
from utils.message_box import MessageBox

logging.basicConfig(filename="stellar-csv-creator.log", format=f"%(asctime)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%SZ", level=logging.INFO)


class CSVCreator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CSVCreator, self).__init__(parent)
        self.version = "0.3.0"
        sys.excepthook = self.error_handler

        self.app = QtWidgets.QApplication([])
        self.setupUi(self)

        # Set config
        self.config_path = "config.json"
        self.config = json.load(open(self.config_path))
        self.csv_config = self.config["CSV"]
        self.app_config = self.config["APP"]
        self.theme = self.app_config["THEME"]

        # Configure GUI
        self.setWindowTitle(f"Stellar CSV Creator v{self.version}")
        self.app.setStyle('Fusion')
        self.window_icon = QtGui.QIcon()
        if self.theme == "dark":
            self.dark_theme()
            self.window_icon_file = "gui/icons/stellar_dark.ico"
        else:
            self.window_icon_file = "gui/icons/stellar_default.ico"

        # Set icons
        self.window_icon.addPixmap(QtGui.QPixmap(self.window_icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(self.window_icon)

        # Create address book DB
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('addresses.db')
        if not self.db.open():
            self.mb.message_box("Unable to establish a database connection.\n"
                                "This example needs SQLite support. Please read "
                                "the Qt SQL driver documentation for information "
                                "how to build it.\n\n", critical=True)

        self.query = QtSql.QSqlQuery()
        self.query.exec_("""CREATE TABLE IF NOT EXISTS addresses (id integer primary key autoincrement,
                                                         Nickname VARCHAR(20),
                                                        Address VARCHAR(20))""")

        # Load address book table
        self.view = self.tableAddresses
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("addresses")
        self.load_addresses()

        # Address book context menu
        self.useAction = QtWidgets.QAction("Use", None)
        self.editAction = QtWidgets.QAction("Edit", None)
        self.deleteAction = QtWidgets.QAction("Delete", None)
        self.tableAddresses.addAction(self.useAction)
        self.tableAddresses.addAction(self.editAction)
        self.tableAddresses.addAction(self.deleteAction)

        # Configure address book table
        self.tableAddresses.installEventFilter(self)
        self.tableAddresses.verticalHeader().setVisible(False)
        self.tableAddresses.setColumnHidden(0, True)
        self.tableAddresses.setColumnWidth(1, 90)
        self.tableAddresses.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableAddresses.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Backend functions
        self.get_config()
        self.make_links()
        self.mb = MessageBox()

    def load_addresses(self):
        self.model.select()
        self.view.setModel(self.model)

    def add_address(self):
        address = self.ABAddress.text()
        nickname = self.ABNickname.text()
        self.query.exec_(f"INSERT INTO addresses (Nickname, Address) values('{nickname}', '{address}')")
        self.ABAddress.clear()
        self.ABNickname.clear()
        self.load_addresses()

    def edit_address(self):
        index = self.tableAddresses.selectionModel().currentIndex()
        self.tableAddresses.edit(index)

    def use_address(self):
        index = self.tableAddresses.selectionModel().currentIndex()
        value = index.sibling(index.row(), 2).data()
        self.Address.setText(value)

    def delete_address(self):
        index = self.tableAddresses.selectionModel().currentIndex()
        self.model.removeRow(index.row())
        self.load_addresses()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Delete:
                index = self.tableAddresses.selectionModel().currentIndex()
                self.model.removeRow(index.row())
                self.load_addresses()
                return True
        return False

    def dark_theme(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(90, 90, 90))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(90, 90, 90))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(90, 90, 90))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.blue)
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(90, 90, 90))
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(17, 31, 54))
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Link, QtCore.Qt.yellow)
        palette.setColor(QtGui.QPalette.LinkVisited, QtCore.Qt.yellow)

        self.setPalette(palette)
        self.app.setPalette(palette)
        self.CreateCSV.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")
        self.GetBalance.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")
        self.radioButtonDarkMode.setStyleSheet("QRadioButton:disabled {color: #a1a1a1}")
        self.radioButtonLightMode.setStyleSheet("QRadioButton:disabled {color: #a1a1a1}")
        self.addAddress.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")
        self.app.setStyleSheet("QMenu {margin:5px}"
                               "QMenu::item {padding: 2px 20px 2px 20px}"
                               "QMenu::item:disabled {"
                               "color: #a1a1a1;"
                               "border: none}"
                               "QMenu::item:selected {background: rgb(17, 31, 54)}")

    def get_config(self):
        rb_light = self.radioButtonLightMode
        rb_dark = self.radioButtonDarkMode

        self.Source.setText(self.csv_config["SOURCE"])
        self.Memo.setText(self.csv_config["MEMO"])
        self.MinThresh.setText(self.csv_config["MIN_THRESH"])
        self.MaxThresh.setText(self.csv_config["MAX_THRESH"])

        if self.theme == "default":
            rb_light.click()
            rb_light.setDisabled(True)
        if self.theme == "dark":
            rb_dark.click()
            rb_dark.setDisabled(True)

        if rb_dark.isChecked() and self.theme == "default":
            rb_light.setEnabled(True)
            rb_light.click()
            rb_light.setDisabled(True)
        if rb_light.isChecked() and self.theme == "dark":
            rb_dark.setEnabled(True)
            rb_dark.click()
            rb_dark.setDisabled(True)

    def make_links(self):
        # Menu bar
        self.actionExit.triggered.connect(self.exit_app)
        self.actionAbout.triggered.connect(self.about_dialog)
        self.actionCheck_for_updates.triggered.connect(self.check_for_updates)
        # Main tab
        self.CreateCSV.clicked.connect(self.create_csv)
        self.GetBalance.clicked.connect(self.get_balance)
        self.Address.textChanged.connect(self.enable_buttons)
        self.Address.returnPressed.connect(self.CreateCSV.click)
        self.Address.textChanged['QString'].connect(self.enable_buttons)
        self.StartDate.textChanged.connect(self.enable_buttons)
        # Addresses tab
        self.ABAddress.returnPressed.connect(self.addAddress.click)
        self.ABAddress.textChanged.connect(self.enable_buttons)
        self.ABAddress.textChanged['QString'].connect(self.enable_buttons)
        self.addAddress.clicked.connect(self.add_address)
        self.useAction.triggered.connect(self.use_address)
        self.editAction.triggered.connect(self.edit_address)
        self.deleteAction.triggered.connect(self.delete_address)
        # Settings tab
        self.SaveSettings.clicked.connect(self.save_settings)
        self.resetButton.clicked.connect(self.get_config)

    def enable_buttons(self):
        if self.Address.text():
            self.GetBalance.setEnabled(True)
        else:
            self.GetBalance.setEnabled(False)

        if self.Address.text() and self.StartDate.text():
            self.CreateCSV.setEnabled(True)
        else:
            self.CreateCSV.setEnabled(False)

        if self.ABAddress.text():
            self.addAddress.setEnabled(True)
        else:
            self.addAddress.setEnabled(False)

    def about_dialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        about = Ui_Dialog()
        about.setupUi(Dialog)
        Dialog.setWindowIcon(self.window_icon)
        about.labelVersion.setText(f"<html><head/><body><p>Stellar CSV Creator v{self.version}</p></body></html>")
        Dialog.show()
        Dialog.exec_()

    def check_for_updates(self):
        session = requests_cache.CachedSession(cache_name="update_cache", expire_after=3600, extension=".db")
        with session:
            response = session.get("https://api.github.com/repos/usertxt/stellar-csv-creator/releases")
            response = response.json()
            new_version = response[0]["tag_name"].replace("v", "")
            if new_version > self.version:
                self.mb.message_box("<a href=\"https://github.com/usertxt/stellar-csv-creator/releases/latest\">"
                                    f"Version {new_version} is available</a>", info=True)
            else:
                self.mb.message_box("You are using the latest release", info=True)

    def create_csv(self):
        if not self.Address.text() or not self.StartDate.text():
            return self.console("Enter your address and your start date!", error=True)
        else:
            pass
        url = f"https://horizon.stellar.org/accounts/{self.Address.text()}/effects?cursor=&limit=100&order=desc"
        main_response = requests.get(url).json()
        main_response = main_response["_embedded"]["records"]

        start_date = datetime.strptime(self.StartDate.text(), "%Y-%m-%d")
        end_date = datetime.utcnow()
        start_date_console = datetime.strftime(start_date, "%Y-%m-%d")
        end_date_console = datetime.strftime(end_date, "%Y-%m-%d")

        top_row = ("Date", "Action", "Volume", "Symbol", "Source", "Memo")

        try:
            with open(f"{self.Address.text()}.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(top_row)

            if self.EndDate.text():
                end_date = datetime.strptime(self.EndDate.text(), "%Y-%m-%d")
                end_date_console = datetime.strftime(end_date, "%Y-%m-%d")

            self.console(f"Creating CSV with transactions from {start_date_console} to {end_date_console}", log=True)
            logging.info(top_row)
            self.output.append(str(top_row))
            for tx in main_response:
                created_at = tx["created_at"]
                amount = tx["amount"]

                threshold_min = float(self.csv_config["MIN_THRESH"])
                threshold_max = float(self.csv_config["MAX_THRESH"])

                dates = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
                dates_formatted = datetime.strptime(dates, "%Y-%m-%d")

                if float(amount) > threshold_max or float(amount) < threshold_min:
                    pass
                else:
                    if start_date <= dates_formatted <= end_date:
                        action = "INCOME"
                        symbol = "XLM"
                        source = self.csv_config["SOURCE"]
                        memo = self.csv_config["MEMO"]
                        rows = (created_at, action, amount, symbol, source, memo)
                        logging.info(rows)
                        self.output.append(str(rows))
                        with open(f"{self.Address.text()}.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(rows)
                self.statusbar.showMessage("CSV created", msecs=3000)

        except Exception as e:
            e = str(e)
            if e == "'amount'":
                e = e.replace("'amount'", "==End of transactions from selected date range==")
                self.console(e, log=True)
            else:
                self.console(e, error=True, log=True)

    def get_balance(self):
        try:
            if not self.Address.text():
                return self.console("Enter your address into the address field!", error=True)
            else:
                pass
            url = f"https://horizon.stellar.org/accounts/{self.Address.text()}"
            response = requests.get(url).json()
            balance_response = response["balances"][0]["balance"]
            if self.theme == "dark":
                font_color = "orange"
            else:
                font_color = "black"
            self.console(f"<html><font color={font_color}>Balance: {balance_response} XLM</html>")

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.console("Unable to retrieve balance. Check the accuracy of your address.", error=True, log=True)
            self.console(e, error=True, log=True)

    def save_settings(self):
        try:
            self.csv_config["MIN_THRESH"] = self.MinThresh.text()
            self.csv_config["MAX_THRESH"] = self.MaxThresh.text()
            self.csv_config["SOURCE"] = self.Source.text()
            self.csv_config["MEMO"] = self.Memo.text()
            if self.radioButtonLightMode.isChecked():
                self.app_config["THEME"] = "default"
            else:
                self.app_config["THEME"] = "dark"
            with open(self.config_path, "w") as updated_config:
                json.dump(self.config, updated_config, indent=2, sort_keys=False, ensure_ascii=True)
            self.statusbar.showMessage("Settings saved", msecs=3000)

            if self.radioButtonLightMode.isChecked() and self.theme == "dark":
                self.mb.theme_change_msgbox()
            elif self.radioButtonDarkMode.isChecked() and self.theme == "default":
                self.mb.theme_change_msgbox()

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.statusbar.showMessage("Unable to save settings", msecs=3000)
            self.console(e, error=True, log=True)

    def console(self, info, error=False, log=False):
        console_append = f"<html><b>{info}</b></html>"
        if log:
            logging.info(info)
        if error and self.theme == "default":
            console_append = f"<html><font color=red><b>{info}</b></font></html>"
        elif error and self.theme == "dark":
            console_append = f"<html><font color=#ff4f4f><b>{info}</b></font></html>"

        return self.output.append(console_append)

    def exit_app(self):
        sys.exit()

    def error_handler(self, exc_type, exc_value, exc_traceback):
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
        self.console("CRITICAL ERROR: Check log file for full details", error=True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = CSVCreator()
    CSVCreator.show(ui)
    sys.exit(app.exec_())
