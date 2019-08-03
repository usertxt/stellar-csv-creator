from PyQt5 import QtGui, QtCore, QtWidgets
from gui.main_window import Ui_MainWindow
from gui.about import Ui_Dialog
from gui.edit_address import EditDialog
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

        # Set theme
        if self.theme == "dark":
            self.dark_theme()

        # Configure Address Book
        self.useAction = QtWidgets.QAction("Use", None)
        self.editAction = QtWidgets.QAction("Edit", None)
        self.deleteAction = QtWidgets.QAction("Delete", None)
        self.ui.listAddress.addAction(self.useAction)
        self.ui.listAddress.addAction(self.editAction)
        self.ui.listAddress.addAction(self.deleteAction)
        self.ui.listAddress.setColumnWidth(0, 90)
        self.ui.listAddress.verticalHeader().setVisible(False)
        self.ui.listAddress.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.ui.listAddress.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.listAddress.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Backend commands
        self.get_config()
        self.ui.clearButton.hide()
        self.load_addresses()
        self.make_links()

        MainWindow.show()
        sys.exit(self.app.exec_())

    def load_addresses(self):
        try:
            with open(self.saved_addresses, "r", newline='') as csv_file:
                self.ui.listAddress.setRowCount(0)
                self.ui.listAddress.setColumnCount(2)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.ui.listAddress.rowCount()
                    self.ui.listAddress.insertRow(row)
                    if len(row_data) > 2:
                        self.ui.listAddress.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(stuff)
                        self.ui.listAddress.setItem(row, column, item)
        except IOError:
            f = open(self.saved_addresses, "w", newline='')
            f.close()

    def add_address(self):
        try:
            nickname = self.ui.nicknameAddress.text()
            address = self.ui.ABAddress.text()
            if len(address) != 0:
                fields = [nickname, address]
                with open(self.saved_addresses, "a", newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(fields)
                self.load_addresses()
        except Exception as e:
            print(e)

    def edit_address(self):
        try:
            dialog = EditDialog()
            row = self.ui.listAddress.currentRow()
            dialog.nickname.setText(self.ui.listAddress.item(row, 0).text())
            dialog.address.setText(self.ui.listAddress.item(row, 1).text())
            dialog.exec_()

            new_nickname = dialog.getInputs()[0]
            new_address = dialog.getInputs()[1]
            fields = [new_nickname, new_address]
            column = self.ui.listAddress.currentColumn()
            address = self.ui.listAddress.item(row, 1).text()
            self.ui.listAddress.takeItem(row, column)

            with open(self.saved_addresses, "r") as f:
                data = list(csv.reader(f))

            with open(self.saved_addresses, "w", newline='') as f:
                writer = csv.writer(f)
                for row in data:
                    if row[1] != address:
                        writer.writerow(row)
                writer.writerow(fields)

            self.load_addresses()
        except Exception as e:
            print(e)

    def use_address(self):
        row = self.ui.listAddress.currentRow()
        self.ui.Address.setText(self.ui.listAddress.item(row, 1).text())

    def delete_address(self):
        try:
            row = self.ui.listAddress.currentRow()
            column = self.ui.listAddress.currentColumn()
            address = self.ui.listAddress.item(row, 1).text()
            self.ui.listAddress.takeItem(row, column)
            with open(self.saved_addresses, "r") as f:
                data = list(csv.reader(f))

            with open(self.saved_addresses, "w", newline='') as f:
                writer = csv.writer(f)
                for row in data:
                    if row[1] != address:
                        writer.writerow(row)
            self.load_addresses()
        except Exception as e:
            print(e)

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
        self.ui.CreateCSV.clicked.connect(self.create_csv)
        self.ui.GetBalance.clicked.connect(self.get_balance)
        self.ui.SaveSettings.clicked.connect(self.save_settings)
        self.ui.actionExit.triggered.connect(self.exit_app)
        self.ui.actionAbout.triggered.connect(self.about_dialog)
        self.ui.Address.textChanged.connect(self.enable_buttons)
        self.ui.StartDate.textChanged.connect(self.enable_buttons)
        self.ui.resetButton.clicked.connect(self.get_config)
        self.ui.clearButton.clicked.connect(self.clear_button)
        self.ui.Address.textChanged['QString'].connect(self.ui.clearButton.show)
        self.ui.actionCheck_for_updates.triggered.connect(self.check_for_updates)
        self.ui.addAddress.clicked.connect(self.add_address)
        self.useAction.triggered.connect(self.use_address)
        self.editAction.triggered.connect(self.edit_address)
        self.deleteAction.triggered.connect(self.delete_address)
        self.ui.listAddress.itemActivated.connect(self.use_address)

    def clear_button(self):
        self.ui.Address.clear()
        self.ui.clearButton.hide()

    def enable_buttons(self):
        if self.ui.Address.text():
            self.ui.GetBalance.setEnabled(True)
        else:
            self.ui.GetBalance.setEnabled(False)
        if self.ui.Address.text() and self.ui.StartDate.text():
            self.ui.CreateCSV.setEnabled(True)
        else:
            self.ui.CreateCSV.setEnabled(False)

    def message_box(self, text, warning=False, info=False):
        msgBox = QtWidgets.QMessageBox()
        msgBox_icon = QtGui.QIcon()
        msgBox_icon.addPixmap(QtGui.QPixmap("gui/icons/stellar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msgBox.setWindowIcon(msgBox_icon)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setWindowTitle("Notice")
        if warning:
            msgBox.setIcon(msgBox.Warning)
        if info:
            msgBox.setIcon(msgBox.Information)
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
                self.message_box("Restart required to change theme", warning=True)
            elif self.ui.radioButtonDarkMode.isChecked() and self.theme == "default":
                self.message_box("Restart required to change theme", warning=True)

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
        if error:
            console_append = f"<html><font color=red><b>{info}</b></font></html>"

        return self.ui.output.append(console_append)

    def exit_app(self):
        sys.exit()

    def error_handler(self, exc_type, exc_value, exc_traceback):
        logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
        self.console("CRITICAL ERROR: Check log file for full details", error=True)


if __name__ == "__main__":
    CSVCreator()
