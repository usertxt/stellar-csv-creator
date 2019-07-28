from PyQt5 import QtGui, QtCore, QtWidgets
from gui.main_window import Ui_MainWindow
from gui.about import Ui_Dialog
from datetime import datetime
import logging
import csv
import json
import requests
import sys

VERSION = "0.1.0"

logging.basicConfig(filename="stellar-csv-creator.log", format=f"%(asctime)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%SZ", level=logging.INFO)


class CSVCreator:
    def __init__(self):
        sys.excepthook = self.error_handler
        self.config_path = "config.json"
        self.config = json.load(open(self.config_path))
        self.csv_config = self.config["CSV"]

        self._translate = QtCore.QCoreApplication.translate
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle(self._translate("MainWindow", f"Stellar CSV Creator v{VERSION}"))
        self.make_links()
        self.get_config()

        MainWindow.show()
        sys.exit(app.exec_())

    def get_config(self):
        self.ui.Source.setText(self._translate("MainWindow", self.csv_config["SOURCE"]))
        self.ui.Memo.setText(self._translate("MainWindow", self.csv_config["MEMO"]))
        self.ui.MinThresh.setText(self._translate("MainWindow", self.csv_config["MIN_THRESH"]))
        self.ui.MaxThresh.setText(self._translate("MainWindow", self.csv_config["MAX_THRESH"]))

    def make_links(self):
        self.ui.CreateCSV.clicked.connect(self.create_csv)
        self.ui.GetBalance.clicked.connect(self.get_balance)
        self.ui.SaveSettings.clicked.connect(self.save_settings)
        self.ui.actionExit.triggered.connect(self.exit_app)
        self.ui.actionAbout.triggered.connect(self.about_dialog)
        self.ui.Address.textChanged.connect(self.enable_buttons)
        self.ui.StartDate.textChanged.connect(self.enable_buttons)

    def enable_buttons(self):
        if self.ui.Address.text():
            self.ui.GetBalance.setEnabled(True)
        if self.ui.Address.text() and self.ui.StartDate.text():
            self.ui.CreateCSV.setEnabled(True)

    def about_dialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        about = Ui_Dialog()
        about.setupUi(Dialog)
        about.labelVersion.setText(self._translate("Dialog",
                                                   f"<html><head/><body><p>Version {VERSION}</p></body></html>"))
        Dialog.show()
        Dialog.exec_()

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
                self.ui.statusbar.showMessage("CSV created")

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
            self.csv_config["MIN_THRESH"] = self.ui.MinThresh.text()
            self.csv_config["MAX_THRESH"] = self.ui.MaxThresh.text()
            self.csv_config["SOURCE"] = self.ui.Source.text()
            self.csv_config["MEMO"] = self.ui.Memo.text()
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
