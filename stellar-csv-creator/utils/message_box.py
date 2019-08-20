from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import json
import os


class MessageBox:
    def __init__(self):
        self.config_path = "config.json"
        self.config = json.load(open(self.config_path))
        self.theme = self.config["APP"]["THEME"]
        if self.theme == "dark":
            self.icon_file = "gui/icons/stellar_dark.ico"
        else:
            self.icon_file = "gui/icons/stellar_default.ico"

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def message_box(self, text, warning=False, info=False, critical=False):
        msgBox = QtWidgets.QMessageBox()
        msgBox_icon = QtGui.QIcon()
        msgBox_icon.addPixmap(QtGui.QPixmap(self.icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msgBox.setWindowIcon(msgBox_icon)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        if warning:
            msgBox.setWindowTitle("Warning")
            msgBox.setIcon(msgBox.Warning)
        if info:
            msgBox.setWindowTitle("Notice")
            msgBox.setIcon(msgBox.Information)
        if critical:
            msgBox.setWindowTitle("Error")
            msgBox.setIcon(msgBox.Critical)
        msgBox.setText(text)
        msgBox.addButton(QtWidgets.QPushButton('OK'), QtWidgets.QMessageBox.YesRole)
        msgBox.exec_()

    def theme_change_msgbox(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox_icon = QtGui.QIcon()
        msgBox_icon.addPixmap(QtGui.QPixmap(self.icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msgBox.setWindowIcon(msgBox_icon)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setWindowTitle("App Restart Required")
        msgBox.setIcon(msgBox.Warning)
        msgBox.setText("App restart required to change theme")
        restart = msgBox.addButton("Restart", QtWidgets.QMessageBox.YesRole)
        cancel = msgBox.addButton("Cancel", QtWidgets.QMessageBox.RejectRole)
        msgBox.exec_()
        if msgBox.clickedButton() is restart:
            self.restart_program()
        elif msgBox.clickedButton() is cancel:
            self.message_box("The theme will be changed the next time you run the app", info=True)
