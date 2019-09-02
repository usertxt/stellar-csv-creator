from PySide2 import QtWidgets, QtCore, QtGui

from gui.about import Ui_Dialog


class AboutDialog:
    def __init__(self, version, theme):
        self.version = version
        self.theme = theme
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        if self.theme == "dark":
            link_color = "#007bff"
            self.icon_file = "gui/icons/stellar_dark.ico"
            file = QtCore.QFile(":/qdarkstyle/style.qss")
            file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
            stream = QtCore.QTextStream(file)
            Dialog.setStyleSheet(stream.readAll())
        else:
            link_color = "#0000ff"
            self.icon_file = "gui/icons/stellar_default.ico"

        self.window_icon = QtGui.QIcon()
        self.window_icon.addPixmap(QtGui.QPixmap(self.icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(self.window_icon)
        about = Ui_Dialog()
        about.setupUi(Dialog)
        about.labelVersion.setText(f"Stellar CSV Creator v{self.version}")
        about.labelWebsiteLink.setText("<a href=\"http://usertxt.com/stellar-csv-creator\">"
                                       f"<span style=\" text-decoration: underline; color:{link_color};\">"
                                       "usertxt.com/stellar-csv-creator</span></a>")
        about.labelSourceCodeLink.setText("<a href=\"https://github.com/usertxt/stellar-csv-creator\"><span style=\""
                                          f" text-decoration: underline; color:{link_color};\">Source Code</span></a>")
        about.labelLicenseLink.setText("<a href=\"https://github.com/usertxt/stellar-csv-creator/blob/master/LICENSE\">"
                                       f"<span style=\" text-decoration: underline; color:{link_color};\">"
                                       f"The MIT License</span></a>")
        Dialog.show()
        Dialog.exec_()