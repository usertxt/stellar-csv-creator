from PySide2 import QtWidgets, QtCore, QtGui

from gui.about import Ui_Dialog


class AboutDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, version, theme, link_color, icon_file, parent=None):
        super(AboutDialog, self).__init__(parent)

        # Get variables from main
        self.version = version
        self.theme = theme
        self.window_icon_file = icon_file

        # Set window flags
        self.setWindowFlags(
            QtCore.Qt.WindowSystemMenuHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint
        )

        # Check theme
        if self.theme == "dark":
            file = QtCore.QFile(":/qdarkstyle/style.qss")
            file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
            stream = QtCore.QTextStream(file)
            self.setStyleSheet(stream.readAll())

        # Set dialog ui
        self.window_icon = QtGui.QIcon()
        self.window_icon.addPixmap(QtGui.QPixmap(self.window_icon_file), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(self.window_icon)
        self.setupUi(self)
        self.labelVersion.setText(f"Stellar CSV Creator v{self.version}")
        self.labelWebsiteLink.setText("<a href=\"http://usertxt.com/stellar-csv-creator\">"
                                       f"<span style=\" text-decoration: underline; color:{link_color};\">"
                                       "usertxt.com/stellar-csv-creator</span></a>")
        self.labelSourceCodeLink.setText("<a href=\"https://github.com/usertxt/stellar-csv-creator\"><span style=\""
                                          f" text-decoration: underline; color:{link_color};\">Source Code</span></a>")
        self.labelLicenseLink.setText("<a href=\"https://github.com/usertxt/stellar-csv-creator/blob/master/LICENSE\">"
                                       f"<span style=\" text-decoration: underline; color:{link_color};\">"
                                       f"The MIT License</span></a>")
