from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labelEndDate = QtWidgets.QLabel(self.tab)
        self.labelEndDate.setGeometry(QtCore.QRect(115, 10, 50, 20))
        self.labelEndDate.setObjectName("labelEndDate")
        self.EndDate = QtWidgets.QLineEdit(self.tab)
        self.EndDate.setGeometry(QtCore.QRect(100, 30, 75, 20))
        self.EndDate.setObjectName("EndDate")
        self.CreateCSV = QtWidgets.QPushButton(self.tab)
        self.CreateCSV.setEnabled(False)
        self.CreateCSV.setGeometry(QtCore.QRect(480, 60, 75, 20))
        self.CreateCSV.setObjectName("CreateCSV")
        self.GetBalance = QtWidgets.QPushButton(self.tab)
        self.GetBalance.setEnabled(False)
        self.GetBalance.setGeometry(QtCore.QRect(480, 90, 75, 20))
        self.GetBalance.setObjectName("GetBalance")
        self.StartDate = QtWidgets.QLineEdit(self.tab)
        self.StartDate.setGeometry(QtCore.QRect(20, 30, 75, 20))
        self.StartDate.setText("")
        self.StartDate.setObjectName("StartDate")
        self.labelStartDate = QtWidgets.QLabel(self.tab)
        self.labelStartDate.setGeometry(QtCore.QRect(32, 10, 50, 20))
        self.labelStartDate.setObjectName("labelStartDate")
        self.output = QtWidgets.QTextBrowser(self.tab)
        self.output.setGeometry(QtCore.QRect(20, 60, 450, 141))
        self.output.setObjectName("output")
        self.labelAddress = QtWidgets.QLabel(self.tab)
        self.labelAddress.setGeometry(QtCore.QRect(327, 10, 75, 16))
        self.labelAddress.setObjectName("labelAddress")
        self.Address = QtWidgets.QLineEdit(self.tab)
        self.Address.setGeometry(QtCore.QRect(182, 30, 375, 20))
        self.Address.setStatusTip("")
        self.Address.setStyleSheet(" padding-right: 15px;")
        self.Address.setObjectName("Address")
        self.clearButton = QtWidgets.QToolButton(self.tab)
        self.clearButton.setGeometry(QtCore.QRect(540, 32, 16, 16))
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setText("")
        self.clearButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.clearButton.setObjectName("clearButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ABAddress = QtWidgets.QLineEdit(self.tab_2)
        self.ABAddress.setGeometry(QtCore.QRect(110, 30, 375, 20))
        self.ABAddress.setStyleSheet(" padding-right: 15px;")
        self.ABAddress.setObjectName("ABAddress")
        self.addAddress = QtWidgets.QPushButton(self.tab_2)
        self.addAddress.setEnabled(False)
        self.addAddress.setGeometry(QtCore.QRect(497, 30, 75, 20))
        self.addAddress.setObjectName("addAddress")
        self.ABNickname = QtWidgets.QLineEdit(self.tab_2)
        self.ABNickname.setGeometry(QtCore.QRect(6, 30, 91, 20))
        self.ABNickname.setObjectName("ABNickname")
        self.labelABAddress = QtWidgets.QLabel(self.tab_2)
        self.labelABAddress.setGeometry(QtCore.QRect(260, 10, 75, 16))
        self.labelABAddress.setObjectName("labelABAddress")
        self.labelABNickname = QtWidgets.QLabel(self.tab_2)
        self.labelABNickname.setGeometry(QtCore.QRect(25, 10, 48, 16))
        self.labelABNickname.setObjectName("labelABNickname")
        self.tableAddresses = QtWidgets.QTableView(self.tab_2)
        self.tableAddresses.setGeometry(QtCore.QRect(6, 55, 566, 151))
        self.tableAddresses.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableAddresses.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAddresses.setObjectName("tableAddresses")
        self.ABclearButton = QtWidgets.QToolButton(self.tab_2)
        self.ABclearButton.setGeometry(QtCore.QRect(468, 32, 16, 16))
        self.ABclearButton.setAutoFillBackground(False)
        self.ABclearButton.setText("")
        self.ABclearButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.ABclearButton.setObjectName("ABclearButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.labelSource = QtWidgets.QLabel(self.tab_3)
        self.labelSource.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.labelSource.setObjectName("labelSource")
        self.labelMinThresh = QtWidgets.QLabel(self.tab_3)
        self.labelMinThresh.setGeometry(QtCore.QRect(20, 60, 100, 16))
        self.labelMinThresh.setObjectName("labelMinThresh")
        self.labelMemo = QtWidgets.QLabel(self.tab_3)
        self.labelMemo.setGeometry(QtCore.QRect(150, 10, 81, 16))
        self.labelMemo.setObjectName("labelMemo")
        self.labelMaxThresh = QtWidgets.QLabel(self.tab_3)
        self.labelMaxThresh.setGeometry(QtCore.QRect(150, 60, 100, 16))
        self.labelMaxThresh.setObjectName("labelMaxThresh")
        self.Source = QtWidgets.QLineEdit(self.tab_3)
        self.Source.setGeometry(QtCore.QRect(20, 28, 113, 20))
        self.Source.setObjectName("Source")
        self.Memo = QtWidgets.QLineEdit(self.tab_3)
        self.Memo.setGeometry(QtCore.QRect(150, 28, 113, 20))
        self.Memo.setObjectName("Memo")
        self.MinThresh = QtWidgets.QLineEdit(self.tab_3)
        self.MinThresh.setGeometry(QtCore.QRect(20, 78, 113, 20))
        self.MinThresh.setObjectName("MinThresh")
        self.MaxThresh = QtWidgets.QLineEdit(self.tab_3)
        self.MaxThresh.setGeometry(QtCore.QRect(150, 78, 113, 20))
        self.MaxThresh.setObjectName("MaxThresh")
        self.SaveSettings = QtWidgets.QPushButton(self.tab_3)
        self.SaveSettings.setGeometry(QtCore.QRect(20, 110, 75, 20))
        self.SaveSettings.setObjectName("SaveSettings")
        self.radioButtonLightMode = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonLightMode.setGeometry(QtCore.QRect(300, 28, 82, 17))
        self.radioButtonLightMode.setObjectName("radioButtonLightMode")
        self.radioButtonDarkMode = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonDarkMode.setGeometry(QtCore.QRect(300, 50, 82, 17))
        self.radioButtonDarkMode.setObjectName("radioButtonDarkMode")
        self.labelTheme = QtWidgets.QLabel(self.tab_3)
        self.labelTheme.setGeometry(QtCore.QRect(300, 10, 47, 13))
        self.labelTheme.setObjectName("labelTheme")
        self.resetButton = QtWidgets.QPushButton(self.tab_3)
        self.resetButton.setGeometry(QtCore.QRect(100, 110, 75, 20))
        self.resetButton.setToolTip("")
        self.resetButton.setObjectName("resetButton")
        self.tabWidget.addTab(self.tab_3, "")
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
        self.actionCheck_for_updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.StartDate)
        MainWindow.setTabOrder(self.StartDate, self.EndDate)
        MainWindow.setTabOrder(self.EndDate, self.Address)
        MainWindow.setTabOrder(self.Address, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.CreateCSV)
        MainWindow.setTabOrder(self.CreateCSV, self.GetBalance)
        MainWindow.setTabOrder(self.GetBalance, self.output)
        MainWindow.setTabOrder(self.output, self.ABNickname)
        MainWindow.setTabOrder(self.ABNickname, self.ABAddress)
        MainWindow.setTabOrder(self.ABAddress, self.ABclearButton)
        MainWindow.setTabOrder(self.ABclearButton, self.addAddress)
        MainWindow.setTabOrder(self.addAddress, self.tableAddresses)
        MainWindow.setTabOrder(self.tableAddresses, self.Source)
        MainWindow.setTabOrder(self.Source, self.Memo)
        MainWindow.setTabOrder(self.Memo, self.MinThresh)
        MainWindow.setTabOrder(self.MinThresh, self.MaxThresh)
        MainWindow.setTabOrder(self.MaxThresh, self.radioButtonLightMode)
        MainWindow.setTabOrder(self.radioButtonLightMode, self.radioButtonDarkMode)
        MainWindow.setTabOrder(self.radioButtonDarkMode, self.SaveSettings)
        MainWindow.setTabOrder(self.SaveSettings, self.resetButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.labelEndDate.setText(_translate("MainWindow", "End Date"))
        self.EndDate.setToolTip(_translate("MainWindow", "End Date (optional): Create a range of transactions received with a specific end date"))
        self.EndDate.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.CreateCSV.setToolTip(_translate("MainWindow", "Create CSV file with chosen parameters"))
        self.CreateCSV.setText(_translate("MainWindow", "Create CSV"))
        self.GetBalance.setToolTip(_translate("MainWindow", "Print the balance"))
        self.GetBalance.setText(_translate("MainWindow", "Get Balance"))
        self.StartDate.setToolTip(_translate("MainWindow", "Start Date (required): The date of the oldest transaction received"))
        self.StartDate.setPlaceholderText(_translate("MainWindow", "YYYY-MM-DD"))
        self.labelStartDate.setText(_translate("MainWindow", "Start Date"))
        self.output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Start Date</span> (required): The date of the oldest transaction received</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">End Date</span> (optional): Create a range of transactions received with a specific end date</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Stellar Address</span> (required): A Stellar address to receive transactions from</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labelAddress.setText(_translate("MainWindow", "Stellar Address"))
        self.Address.setToolTip(_translate("MainWindow", "Stellar Address (required): A Stellar address to receive transactions from"))
        self.clearButton.setToolTip(_translate("MainWindow", "Clear address"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.ABAddress.setToolTip(_translate("MainWindow", "Stellar address (required)"))
        self.addAddress.setToolTip(_translate("MainWindow", "Add to address book"))
        self.addAddress.setText(_translate("MainWindow", "Add"))
        self.ABNickname.setToolTip(_translate("MainWindow", "Nickname (optional)"))
        self.labelABAddress.setText(_translate("MainWindow", "Stellar Address"))
        self.labelABNickname.setText(_translate("MainWindow", "Nickname (optional)"))
        self.ABclearButton.setToolTip(_translate("MainWindow", "Clear address"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Address Book"))
        self.labelSource.setText(_translate("MainWindow", "Source"))
        self.labelMinThresh.setText(_translate("MainWindow", "Minimum Threshold"))
        self.labelMemo.setText(_translate("MainWindow", "Memo"))
        self.labelMaxThresh.setText(_translate("MainWindow", "Maximum Threshold"))
        self.SaveSettings.setToolTip(_translate("MainWindow", "Save chosen settings"))
        self.SaveSettings.setText(_translate("MainWindow", "Save Settings"))
        self.radioButtonLightMode.setText(_translate("MainWindow", "Light"))
        self.radioButtonDarkMode.setText(_translate("MainWindow", "Dark"))
        self.labelTheme.setText(_translate("MainWindow", "Theme"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCheck_for_updates.setText(_translate("MainWindow", "Check for updates"))
