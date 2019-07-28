from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 260)
        MainWindow.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stellar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labelEndDate = QtWidgets.QLabel(self.tab)
        self.labelEndDate.setGeometry(QtCore.QRect(495, 0, 50, 20))
        self.labelEndDate.setObjectName("labelEndDate")
        self.EndDate = QtWidgets.QLineEdit(self.tab)
        self.EndDate.setGeometry(QtCore.QRect(480, 20, 75, 20))
        self.EndDate.setObjectName("EndDate")
        self.CreateCSV = QtWidgets.QPushButton(self.tab)
        self.CreateCSV.setEnabled(False)
        self.CreateCSV.setGeometry(QtCore.QRect(480, 60, 75, 23))
        self.CreateCSV.setObjectName("CreateCSV")
        self.GetBalance = QtWidgets.QPushButton(self.tab)
        self.GetBalance.setEnabled(False)
        self.GetBalance.setGeometry(QtCore.QRect(480, 90, 75, 23))
        self.GetBalance.setObjectName("GetBalance")
        self.StartDate = QtWidgets.QLineEdit(self.tab)
        self.StartDate.setGeometry(QtCore.QRect(400, 20, 75, 20))
        self.StartDate.setText("")
        self.StartDate.setObjectName("StartDate")
        self.labelStartDate = QtWidgets.QLabel(self.tab)
        self.labelStartDate.setGeometry(QtCore.QRect(412, 0, 50, 20))
        self.labelStartDate.setObjectName("labelStartDate")
        self.output = QtWidgets.QTextBrowser(self.tab)
        self.output.setGeometry(QtCore.QRect(20, 60, 450, 101))
        self.output.setObjectName("output")
        self.labelAddress = QtWidgets.QLabel(self.tab)
        self.labelAddress.setGeometry(QtCore.QRect(160, 0, 81, 16))
        self.labelAddress.setObjectName("labelAddress")
        self.Address = QtWidgets.QLineEdit(self.tab)
        self.Address.setGeometry(QtCore.QRect(20, 20, 365, 20))
        self.Address.setStatusTip("")
        self.Address.setObjectName("Address")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelSource = QtWidgets.QLabel(self.tab_2)
        self.labelSource.setGeometry(QtCore.QRect(20, 0, 81, 16))
        self.labelSource.setObjectName("labelSource")
        self.labelMinThresh = QtWidgets.QLabel(self.tab_2)
        self.labelMinThresh.setGeometry(QtCore.QRect(20, 50, 100, 16))
        self.labelMinThresh.setObjectName("labelMinThresh")
        self.labelMemo = QtWidgets.QLabel(self.tab_2)
        self.labelMemo.setGeometry(QtCore.QRect(150, 0, 81, 16))
        self.labelMemo.setObjectName("labelMemo")
        self.labelMaxThresh = QtWidgets.QLabel(self.tab_2)
        self.labelMaxThresh.setGeometry(QtCore.QRect(150, 50, 100, 16))
        self.labelMaxThresh.setObjectName("labelMaxThresh")
        self.Source = QtWidgets.QLineEdit(self.tab_2)
        self.Source.setGeometry(QtCore.QRect(20, 18, 113, 20))
        self.Source.setObjectName("Source")
        self.Memo = QtWidgets.QLineEdit(self.tab_2)
        self.Memo.setGeometry(QtCore.QRect(150, 18, 113, 20))
        self.Memo.setObjectName("Memo")
        self.MinThresh = QtWidgets.QLineEdit(self.tab_2)
        self.MinThresh.setGeometry(QtCore.QRect(20, 68, 113, 20))
        self.MinThresh.setObjectName("MinThresh")
        self.MaxThresh = QtWidgets.QLineEdit(self.tab_2)
        self.MaxThresh.setGeometry(QtCore.QRect(150, 68, 113, 20))
        self.MaxThresh.setObjectName("MaxThresh")
        self.SaveSettings = QtWidgets.QPushButton(self.tab_2)
        self.SaveSettings.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.SaveSettings.setObjectName("SaveSettings")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.Address)
        MainWindow.setTabOrder(self.Address, self.StartDate)
        MainWindow.setTabOrder(self.StartDate, self.EndDate)
        MainWindow.setTabOrder(self.EndDate, self.CreateCSV)
        MainWindow.setTabOrder(self.CreateCSV, self.GetBalance)
        MainWindow.setTabOrder(self.GetBalance, self.output)
        MainWindow.setTabOrder(self.output, self.Source)
        MainWindow.setTabOrder(self.Source, self.Memo)
        MainWindow.setTabOrder(self.Memo, self.MinThresh)
        MainWindow.setTabOrder(self.MinThresh, self.MaxThresh)
        MainWindow.setTabOrder(self.MaxThresh, self.SaveSettings)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.labelEndDate.setText(_translate("MainWindow", "End Date"))
        self.EndDate.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.CreateCSV.setStatusTip(_translate("MainWindow", "Create CSV"))
        self.CreateCSV.setText(_translate("MainWindow", "Create CSV"))
        self.GetBalance.setStatusTip(_translate("MainWindow", "Get Balance"))
        self.GetBalance.setText(_translate("MainWindow", "Get Balance"))
        self.StartDate.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.labelStartDate.setText(_translate("MainWindow", "Start Date"))
        self.output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Instructions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start by putting your Stellar address into the <span style=\" font-weight:600;\">Address</span> field, then input the date of the oldest transation you would like to add to the CSV file into the <span style=\" font-weight:600;\">Start Date</span> field. The <span style=\" font-weight:600;\">Start Date</span> field is required.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labelAddress.setText(_translate("MainWindow", "Stellar Address"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.labelSource.setText(_translate("MainWindow", "Source"))
        self.labelMinThresh.setText(_translate("MainWindow", "Minimum Threshold"))
        self.labelMemo.setText(_translate("MainWindow", "Memo"))
        self.labelMaxThresh.setText(_translate("MainWindow", "Maximum Threshold"))
        self.SaveSettings.setStatusTip(_translate("MainWindow", "Save chosen settings"))
        self.SaveSettings.setText(_translate("MainWindow", "Save Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
