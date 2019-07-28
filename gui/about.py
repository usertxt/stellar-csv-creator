from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        font = QtGui.QFont()
        font.setKerning(True)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stellar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.closeButton = QtWidgets.QDialogButtonBox(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(308, 160, 71, 23))
        self.closeButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.closeButton.setObjectName("closeButton")
        self.labelVersion = QtWidgets.QLabel(Dialog)
        self.labelVersion.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.labelVersion.setObjectName("labelVersion")
        self.labelAbout1 = QtWidgets.QLabel(Dialog)
        self.labelAbout1.setGeometry(QtCore.QRect(10, 40, 381, 21))
        self.labelAbout1.setObjectName("labelAbout1")
        self.labelAbout2 = QtWidgets.QLabel(Dialog)
        self.labelAbout2.setGeometry(QtCore.QRect(10, 60, 381, 20))
        self.labelAbout2.setObjectName("labelAbout2")
        self.labelSourceCodeLink = QtWidgets.QLabel(Dialog)
        self.labelSourceCodeLink.setGeometry(QtCore.QRect(10, 90, 381, 20))
        self.labelSourceCodeLink.setOpenExternalLinks(True)
        self.labelSourceCodeLink.setObjectName("labelSourceCodeLink")
        self.labelLicenseLink = QtWidgets.QLabel(Dialog)
        self.labelLicenseLink.setGeometry(QtCore.QRect(10, 110, 381, 20))
        self.labelLicenseLink.setOpenExternalLinks(True)
        self.labelLicenseLink.setObjectName("labelLicenseLink")

        self.retranslateUi(Dialog)
        self.closeButton.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.labelVersion.setText(_translate("Dialog", "<html><head/><body><p>Version 0.1.0</p></body></html>"))
        self.labelAbout1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8.25pt;\">This program was written with Python and uses Qt for the front-end.</span></p></body></html>"))
        self.labelAbout2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8.25pt;\">This program is completely free, open source, and comes with no warranty.</span></p></body></html>"))
        self.labelSourceCodeLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://github.com/usertxt/stellar-csv-creator\"><span style=\" text-decoration: underline; color:#0000ff;\">Source Code</span></a></p></body></html>"))
        self.labelLicenseLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://github.com/usertxt/stellar-csv-creator/blob/master/LICENSE\"><span style=\" text-decoration: underline; color:#0000ff;\">The MIT License</span></a></p></body></html>"))