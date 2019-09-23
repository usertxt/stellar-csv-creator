import csv
import json
import logging
import sys
import os
import re
from datetime import datetime

import requests
import requests_cache
from PySide2 import QtGui, QtCore, QtWidgets, QtSql

from gui.main_window import Ui_MainWindow
from gui.styles import dark
from utils.about_dialog import AboutDialog
from utils.message_box import MessageBox
from utils.version import version
from utils.util import (date_format, open_path, user_dir, make_dir, setup_config, isfloat, exit_app)


class CSVCreator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CSVCreator, self).__init__(parent)
        self.version = version
        self.log_file = os.path.join(user_dir(), "stellar-csv-creator.log")
        sys.excepthook = self.error_handler

        self.setupUi(self)

        # Set config
        self.config_path = os.path.join(user_dir(), "config.json")
        self.config = json.load(open(self.config_path))
        self.csv_config = self.config["CSV"]
        self.app_config = self.config["APP"]
        self.theme = self.app_config["THEME"]

        # Configure GUI
        self.setWindowTitle(f"Stellar CSV Creator v{self.version}")
        self.window_icon = QtGui.QIcon()

        if self.theme == "dark":
            self.dark_theme()
            self.window_icon_file = "gui/icons/stellar_dark.ico"
            self.link_color = "#007bff"
            self.error_color = "#ff4f4f"
        else:
            self.window_icon_file = "gui/icons/stellar_default.ico"
            self.link_color = "#0000ff"
            self.error_color = "red"

        # Set icons
        self.window_icon.addPixmap(QtGui.QPixmap(self.window_icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(self.window_icon)

        # Set utils instances
        self.mb = MessageBox(self.theme)
        self.date_format = date_format
        self.about_window = None
        self.exit_app = exit_app

        # Create address book DB
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(os.path.join(user_dir(), "addresses.db"))
        if not self.db.open():
            self.mb.message_box("Unable to establish a database connection.\n"
                                "This example needs SQLite support. Please read "
                                "the Qt SQL driver documentation for information "
                                "how to build it.\n\n", critical=True)

        self.query = QtSql.QSqlQuery()
        self.query.exec_("""
                         CREATE TABLE IF NOT EXISTS addresses (id integer primary key autoincrement,
                         Nickname VARCHAR(20),
                         Address VARCHAR(20))
                         """)

        # Load address book table
        self.view = self.tableAddresses
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("addresses")
        self.load_addresses()

        # Address book context menu
        self.useAction = QtWidgets.QAction("Use", self)
        self.editAction = QtWidgets.QAction("Edit", self)
        self.deleteAction = QtWidgets.QAction("Delete", self)
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

    def about_dialog(self):
        if self.about_window is None:
            self.about_window = AboutDialog(self.version, self.theme, self.link_color, self.window_icon_file)
        self.about_window.show()
        self.about_window.activateWindow()

    def dark_theme(self):
        file = QtCore.QFile(":/qdarkstyle/style.qss")
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(file)
        self.setStyleSheet(stream.readAll())

    def folder_dialog(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        if folder != "":
            self.CSVOutputDest.setText(folder)

    def get_config(self):
        rb_light = self.radioButtonLightMode
        rb_dark = self.radioButtonDarkMode

        self.Source.setText(self.csv_config["SOURCE"])
        self.Memo.setText(self.csv_config["MEMO"])
        self.MinThresh.setText(self.csv_config["MIN_THRESH"])
        self.MaxThresh.setText(self.csv_config["MAX_THRESH"])
        self.CSVOutputDest.setText(self.csv_config["DESTINATION"])

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
        self.actionSave_Settings.triggered.connect(self.save_settings)
        self.actionExit.triggered.connect(self.exit_app)
        self.actionAbout.triggered.connect(self.about_dialog)
        self.actionOpen_Log.triggered.connect(lambda: open_path(self.log_file))
        self.actionCheck_for_updates.triggered.connect(self.check_for_updates)
        # Main tab
        self.CreateCSV.clicked.connect(self.create_csv)
        self.GetBalance.clicked.connect(self.get_balance)
        self.Address.textChanged.connect(self.enable_buttons)
        self.Address.returnPressed.connect(self.CreateCSV.click)
        self.Address.textChanged['QString'].connect(self.enable_buttons)
        self.StartDate.textChanged.connect(self.enable_buttons)
        self.output.anchorClicked.connect(lambda: open_path(self.csv_config["DESTINATION"]))
        # Addresses tab
        self.ABAddress.returnPressed.connect(self.addAddress.click)
        self.ABNickname.returnPressed.connect(self.addAddress.click)
        self.ABAddress.textChanged.connect(self.enable_buttons)
        self.ABAddress.textChanged['QString'].connect(self.enable_buttons)
        self.addAddress.clicked.connect(self.add_address)
        self.useAction.triggered.connect(self.use_address)
        self.editAction.triggered.connect(self.edit_address)
        self.deleteAction.triggered.connect(self.delete_address)
        self.tableAddresses.doubleClicked.connect(self.use_address)
        # Settings tab
        self.SaveSettings.clicked.connect(self.save_settings)
        self.resetButton.clicked.connect(self.get_config)
        self.folderButton.clicked.connect(self.folder_dialog)
        self.openFolderButton.clicked.connect(lambda: open_path(self.csv_config["DESTINATION"]))

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

    def check_for_updates(self):
        session = requests_cache.CachedSession(cache_name=os.path.join(user_dir(), "update_cache"), expire_after=3600,
                                               extension=".db")
        with session:
            response = session.get("https://api.github.com/repos/usertxt/stellar-csv-creator/releases")
            response = response.json()
            new_version = response[0]["tag_name"].replace("v", "")
            if new_version > self.version:
                self.mb.message_box("<a href=\"https://github.com/usertxt/stellar-csv-creator/releases/latest\">"
                                    f"<span style=\"text-decoration: underlined; color: {self.link_color}\">Version "
                                    f"{new_version} is available</span></a>", info=True)
            else:
                self.mb.message_box("You are using the latest release", info=True)

    def create_csv(self):
        url = f"https://horizon.stellar.org/accounts/{self.Address.text()}/effects?cursor=&limit=100&order=desc"
        main_response = requests.get(url).json()
        main_response = main_response["_embedded"]["records"]

        start_date = self.date_format(self.StartDate.text(), date_object=True)
        if self.EndDate.text():
            end_date = self.date_format(self.EndDate.text(), date_object=True)
        else:
            end_date = datetime.utcnow()
        start_date_console = self.date_format(start_date, str_object=True)
        end_date_console = self.date_format(end_date, str_object=True)

        threshold_min = float(self.csv_config["MIN_THRESH"])
        threshold_max = float(self.csv_config["MAX_THRESH"])

        csv_file = f"{self.csv_config['DESTINATION']}/{self.Address.text()}.csv"
        top_row = ("Date", "Action", "Volume", "Symbol", "Source", "Memo")
        action = "INCOME"
        symbol = "XLM"
        source = self.csv_config["SOURCE"]
        memo = self.csv_config["MEMO"]
        path = self.csv_config["DESTINATION"]
        filtered_rows = []

        try:
            self.console(f"Searching for transactions from {start_date_console} to {end_date_console}<br>"
                         f"Thresholds are set to {self.csv_config['MIN_THRESH']} (MIN) and "
                         f"{self.csv_config['MAX_THRESH']} (MAX)<p>", log=True)
            for tx in main_response:
                created_at = tx["created_at"]
                amount = tx.get("amount", 0)

                rows = (created_at, action, amount, symbol, source, memo)

                dates = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
                dates_formatted = self.date_format(dates, date_object=True)

                if float(amount) > threshold_max or float(amount) < threshold_min:
                    pass
                elif start_date <= dates_formatted <= end_date:
                    filtered_rows.append(rows)

            if filtered_rows:
                with open(csv_file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(top_row)

                self.console(f"Creating CSV", log=True)
                self.console(str(top_row), log=True, append=True)

                for filtered_tx in filtered_rows:
                    with open(csv_file, "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(filtered_tx)
                    self.console(str(filtered_tx), log=True, append=True)

                self.console(f"End of transactions from {start_date_console} to {end_date_console}<p>")
                self.console(f"Successfully created<br>{self.Address.text()}.csv<br>"
                             f"in folder <a href='{path}'><font color='{self.link_color}'>{path}</font></a><p>",
                             log=True)
                self.statusbar.showMessage("CSV created", timeout=3000)
            else:
                self.console("No transactions found<p>", error=True, log=True)

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.console(e, error=True, log=True)

    def get_balance(self):
        try:
            url = f"https://horizon.stellar.org/accounts/{self.Address.text()}"
            response = requests.get(url).json()
            balance_response = response["balances"][0]["balance"]
            if self.theme == "dark":
                text_color = self.link_color
            else:
                text_color = "black"
            self.console(f"<p><font color=\"{text_color}\">Balance: {balance_response} XLM</font><p>")

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.console("Unable to retrieve balance. Check the accuracy of your address.", error=True, log=True)
            self.console(e, error=True, log=True)

    def save_settings(self):
        try:
            if not (self.MinThresh.text().isdigit() and self.MaxThresh.text().isdigit() or
                    isfloat(self.MinThresh.text()) and isfloat(self.MaxThresh.text())):
                self.statusbar.showMessage("Settings not saved", timeout=3000)
                self.labelMinThresh.setStyleSheet(f"color: {self.error_color};")
                self.labelMaxThresh.setStyleSheet(f"color: {self.error_color};")
                self.mb.message_box("Minimum Threshold and Maximum Threshold must be numbers only", warning=True)
            elif self.MinThresh.text() > self.MaxThresh.text():
                self.statusbar.showMessage("Settings not saved", timeout=3000)
                self.labelMinThresh.setStyleSheet(f"color: {self.error_color};")
                self.labelMaxThresh.setStyleSheet(f"color: {self.error_color};")
                self.mb.message_box("Minimum Threshold must be less than Maximum Threshold", warning=True)
            else:
                self.labelMinThresh.setStyleSheet("")
                self.labelMaxThresh.setStyleSheet("")

                with open(self.config_path, "w") as updated_config:
                    if self.radioButtonLightMode.isChecked():
                        self.app_config["THEME"] = "default"
                    else:
                        self.app_config["THEME"] = "dark"
                    self.csv_config["MIN_THRESH"] = self.MinThresh.text()
                    self.csv_config["MAX_THRESH"] = self.MaxThresh.text()
                    self.csv_config["SOURCE"] = self.Source.text()
                    self.csv_config["MEMO"] = self.Memo.text()
                    self.csv_config["DESTINATION"] = self.CSVOutputDest.text()

                    json.dump(self.config, updated_config, indent=2, sort_keys=False, ensure_ascii=True)
                    self.statusbar.showMessage("Settings saved", timeout=3000)

            if self.radioButtonLightMode.isChecked() and self.theme == "dark":
                self.mb.theme_change_msgbox()
            elif self.radioButtonDarkMode.isChecked() and self.theme == "default":
                self.mb.theme_change_msgbox()

        except Exception as e:
            e = getattr(e, "message", repr(e))
            self.statusbar.showMessage("Unable to save settings", timeout=3000)
            self.console(e, error=True, log=True)

    def console(self, info, error=False, log=False, append=False):
        console_append = f"<b>{info}</b>"
        if log:
            info = re.sub("<[^>]*>", " ", info)
            logging.info(info)
        if error:
            console_append = f"<font color={self.error_color}><b>{info}</b></font>"
        if append:
            console_append = info

        return self.output.append(console_append)

    def error_handler(self, exc_type, exc_value, exc_traceback):
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
        self.console("CRITICAL ERROR: Check log file for full details", error=True)


if __name__ == "__main__":
    make_dir(user_dir())
    make_dir(os.path.join(user_dir(), "CSV Files"))

    log_file = os.path.join(user_dir(), "stellar-csv-creator.log")
    logging.basicConfig(filename=log_file, format=f"%(asctime)s:%(levelname)s:%(message)s",
                        datefmt="%Y-%m-%dT%H:%M:%SZ", level=logging.INFO)
    logging.info("App started")
    setup_config()

    app = QtWidgets.QApplication(sys.argv)
    ui = CSVCreator()
    ui.show()
    sys.exit(app.exec_())
