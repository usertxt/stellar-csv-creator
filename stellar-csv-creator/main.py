from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
from gui.main_window import Ui_MainWindow
from gui.about import Ui_Dialog
from datetime import datetime
import logging
import csv
import json
import requests
import sys

logging.basicConfig(filename="stellar-csv-creator.log", format=f"%(asctime)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%SZ", level=logging.INFO)


class CSVCreator:
    def __init__(self):
        self.version = "0.1.0"
        sys.excepthook = self.error_handler

        # Set config
        self.config_path = "config.json"
        self.config = json.load(open(self.config_path))
        self.csv_config = self.config["CSV"]
        self.app_config = self.config["APP"]
        self.theme = self.app_config["THEME"]
        self.saved_addresses = "saved_addresses.csv"

        # Set up GUI
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle(f"Stellar CSV Creator v{self.version}")
        self.app.setStyle('Fusion')

        # Set icons
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/icons/stellar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("gui/icons/clear-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.clearButton.setIcon(icon1)
        self.ui.ABclearButton.setIcon(icon1)

        # Set theme
        if self.theme == "dark":
            self.dark_theme()

        # Create DB
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('addresses.db')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, ("Cannot open database"),
                                           ("Unable to establish a database connection.\n"
                                            "This example needs SQLite support. Please read "
                                            "the Qt SQL driver documentation for information "
                                            "how to build it.\n\n"
                                            "Click Cancel to exit."),
                                           QtWidgets.QMessageBox.Cancel)
        # return False

        self.query = QtSql.QSqlQuery()
        self.query.exec_("""CREATE TABLE IF NOT EXISTS addresses (id integer primary key autoincrement,
                                                         Nickname VARCHAR(20),
                                                        Address VARCHAR(20))""")

        # Load address book table
        self.view = self.ui.tableAddresses
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("addresses")
        self.load_addresses()

        # Address book context menu
        self.useAction = QtWidgets.QAction("Use", None)
        self.editAction = QtWidgets.QAction("Edit", None)
        self.deleteAction = QtWidgets.QAction("Delete", None)
        self.ui.tableAddresses.addAction(self.useAction)
        self.ui.tableAddresses.addAction(self.editAction)
        self.ui.tableAddresses.addAction(self.deleteAction)

        # Configure address book table
        self.ui.tableAddresses.verticalHeader().setVisible(False)
        self.ui.tableAddresses.setColumnHidden(0, True)
        self.ui.tableAddresses.setColumnWidth(1, 90)
        self.ui.tableAddresses.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableAddresses.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Backend functions
        self.get_config()
        self.ui.clearButton.hide()
        self.ui.ABclearButton.hide()
        self.make_links()

        MainWindow.show()
        sys.exit(self.app.exec_())

    def load_addresses(self):
        self.model.select()
        self.view.setModel(self.model)

    def add_address(self):
        address = self.ui.ABAddress.text()
        nickname = self.ui.ABNickname.text()
        self.query.exec_(f"INSERT INTO addresses (Nickname, Address) values('{nickname}', '{address}')")
        self.load_addresses()

    def edit_address(self):
        index = self.ui.tableAddresses.selectionModel().currentIndex()
        self.ui.tableAddresses.edit(index)

    def use_address(self):
        index = self.ui.tableAddresses.selectionModel().currentIndex()
        value = index.sibling(index.row(), 2).data()
        self.ui.Address.setText(value)

    def delete_address(self):
        index = self.ui.tableAddresses.selectionModel().currentIndex()
        self.model.removeRow(index.row())
        self.load_addresses()

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
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(17, 31, 54).lighter())
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette.Link, QtCore.Qt.yellow)
        palette.setColor(QtGui.QPalette.LinkVisited, QtCore.Qt.yellow)

        self.app.setPalette(palette)
        self.ui.CreateCSV.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")
        self.ui.GetBalance.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")
        self.ui.radioButtonDarkMode.setStyleSheet("QRadioButton:disabled {color: #a1a1a1}")
        self.ui.radioButtonLightMode.setStyleSheet("QRadioButton:disabled {color: #a1a1a1}")
        self.ui.addAddress.setStyleSheet("QPushButton:disabled {color: #a1a1a1}")

    def get_config(self):
        rb_light = self.ui.radioButtonLightMode
        rb_dark = self.ui.radioButtonDarkMode

        self.ui.Source.setText(self.csv_config["SOURCE"])
        self.ui.Memo.setText(self.csv_config["MEMO"])
        self.ui.MinThresh.setText(self.csv_config["MIN_THRESH"])
        self.ui.MaxThresh.setText(self.csv_config["MAX_THRESH"])

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
        self.ui.actionExit.triggered.connect(self.exit_app)
        self.ui.actionAbout.triggered.connect(self.about_dialog)
        self.ui.actionCheck_for_updates.triggered.connect(self.check_for_updates)
        # Main tab
        self.ui.CreateCSV.clicked.connect(self.create_csv)
        self.ui.GetBalance.clicked.connect(self.get_balance)
        self.ui.Address.textChanged.connect(self.enable_buttons)
        self.ui.Address.returnPressed.connect(self.ui.CreateCSV.click)
        self.ui.Address.textChanged['QString'].connect(self.ui.clearButton.show)
        self.ui.StartDate.textChanged.connect(self.enable_buttons)
        self.ui.clearButton.clicked.connect(self.clear_button)
        # Addresses tab
        self.ui.ABAddress.returnPressed.connect(self.ui.addAddress.click)
        self.ui.ABAddress.textChanged.connect(self.enable_buttons)
        self.ui.ABAddress.textChanged['QString'].connect(self.ui.ABclearButton.show)
        self.ui.ABclearButton.clicked.connect(self.clear_button_ab)
        self.ui.addAddress.clicked.connect(self.add_address)
        self.useAction.triggered.connect(self.use_address)
        self.editAction.triggered.connect(self.edit_address)
        self.deleteAction.triggered.connect(self.delete_address)
        # Settings tab
        self.ui.SaveSettings.clicked.connect(self.save_settings)
        self.ui.resetButton.clicked.connect(self.get_config)

    def clear_button(self):
        self.ui.Address.clear()
        self.ui.clearButton.hide()

    def clear_button_ab(self):
        self.ui.ABAddress.clear()
        self.ui.ABclearButton.hide()

    def enable_buttons(self):
        if self.ui.Address.text():
            self.ui.GetBalance.setEnabled(True)
        else:
            self.ui.GetBalance.setEnabled(False)
        if self.ui.Address.text() and self.ui.StartDate.text():
            self.ui.CreateCSV.setEnabled(True)
        else:
            self.ui.CreateCSV.setEnabled(False)
        if self.ui.ABAddress.text():
            self.ui.addAddress.setEnabled(True)
        else:
            self.ui.addAddress.setEnabled(False)

    def message_box(self, text, warning=False, info=False, critical=False):
        msgBox = QtWidgets.QMessageBox()
        msgBox_icon = QtGui.QIcon()
        msgBox_icon.addPixmap(QtGui.QPixmap("gui/icons/stellar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msgBox.setWindowIcon(msgBox_icon)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        if warning:
            msgBox.setWindowTitle("WARNING")
            msgBox.setIcon(msgBox.Warning)
        if info:
            msgBox.setWindowTitle("NOTICE")
            msgBox.setIcon(msgBox.Information)
        if critical:
            msgBox.setWindowTitle("ERROR")
            msgBox.setIcon(msgBox.Critical)
        msgBox.setText(text)
        msgBox.addButton(QtWidgets.QPushButton('OK'), QtWidgets.QMessageBox.YesRole)
        msgBox.exec_()

    def about_dialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        about = Ui_Dialog()
        about.setupUi(Dialog)
        about.labelVersion.setText(f"<html><head/><body><p>Stellar CSV Creator v{self.version}</p></body></html>")
        Dialog.show()
        Dialog.exec_()

    def check_for_updates(self):
        response = requests.get("https://api.github.com/repos/usertxt/stellar-csv-creator/releases").json()
        new_version = response[0]["tag_name"].replace("v", "")
        if new_version > self.version:
            self.message_box("<a href=\"https://github.com/usertxt/stellar-csv-creator/releases/latest\">"
                             f"Version {new_version} is available</a>", info=True)
        else:
            self.message_box("You are using the latest release", info=True)

    def create_csv(self):
        if not self.ui.Address.text() or not self.ui.StartDate.text():
            return self.console("Enter your address and your start date!", error=True)
        else:
            pass
        url = f"https://horizon.stellar.org/accounts/{self.ui.Address.text()}/effects?cursor=&limit=100&order=desc"
        main_response = requests.get(url).json()
        main_response = main_response["_embedded"]["records"]

        start_date = datetime.strptime(self.ui.StartDate.text(), "%Y-%m-%d")
        end_date = datetime.utcnow()
        start_date_console = datetime.strftime(start_date, "%Y-%m-%d")
        end_date_console = datetime.strftime(end_date, "%Y-%m-%d")

        top_row = ("Date", "Action", "Volume", "Symbol", "Source", "Memo")

        try:
            with open(f"{self.ui.Address.text()}.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(top_row)

            if self.ui.EndDate.text():
                end_date = datetime.strptime(self.ui.EndDate.text(), "%Y-%m-%d")
                end_date_console = datetime.strftime(end_date, "%Y-%m-%d")

            self.console(f"Creating CSV with transactions from {start_date_console} to {end_date_console}", log=True)
            logging.info(top_row)
            self.ui.output.append(str(top_row))
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
                        self.ui.output.append(str(rows))
                        with open(f"{self.ui.Address.text()}.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(rows)
                self.ui.statusbar.showMessage("CSV created", msecs=3000)

        except Exception as e:
            e = str(e)
            if e == "'amount'":
                e = e.replace("'amount'", "==End of transactions from selected date range==")
                self.console(e, log=True)
            else:
                self.console(e, error=True, log=True)

    def get_balance(self):
        try:
            if not self.ui.Address.text():
                return self.console("Enter your address into the address field!", error=True)
            else:
                pass
            url = f"https://horizon.stellar.org/accounts/{self.ui.Address.text()}"
            response = requests.get(url).json()
            balance_response = response["balances"][0]["balance"]
            self.console(f"Balance: {balance_response} XLM")

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.console("Unable to retrieve balance. Check the accuracy of your address.", error=True, log=True)
            self.console(e, error=True, log=True)

    def save_settings(self):
        try:
            if self.ui.radioButtonLightMode.isChecked() and self.theme == "dark":
                self.message_box("Restart required to change theme", info=True)
            elif self.ui.radioButtonDarkMode.isChecked() and self.theme == "default":
                self.message_box("Restart required to change theme", info=True)

            self.csv_config["MIN_THRESH"] = self.ui.MinThresh.text()
            self.csv_config["MAX_THRESH"] = self.ui.MaxThresh.text()
            self.csv_config["SOURCE"] = self.ui.Source.text()
            self.csv_config["MEMO"] = self.ui.Memo.text()
            if self.ui.radioButtonLightMode.isChecked():
                self.app_config["THEME"] = "default"
            else:
                self.app_config["THEME"] = "dark"
            with open(self.config_path, "w") as updated_config:
                json.dump(self.config, updated_config, indent=2, sort_keys=False, ensure_ascii=True)
            self.ui.statusbar.showMessage("Settings saved")

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.ui.statusbar.showMessage("Unable to save settings")
            self.console(e, error=True, log=True)

    def console(self, info, error=False, log=False):
        console_append = f"<html><b>{info}</b></html>"
        if log:
            logging.info(info)
        if error and self.theme == "default":
            console_append = f"<html><font color=red><b>{info}</b></font></html>"
        elif error and self.theme == "dark":
            console_append = f"<html><font color=#ff4f4f><b>{info}</b></font></html>"

        return self.ui.output.append(console_append)

    def exit_app(self):
        sys.exit()

    def error_handler(self, exc_type, exc_value, exc_traceback):
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
        self.console("CRITICAL ERROR: Check log file for full details", error=True)


if __name__ == "__main__":
    CSVCreator()
