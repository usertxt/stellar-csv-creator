from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 375)
        MainWindow.setMinimumSize(QtCore.QSize(600, 375))
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelAddress = QtWidgets.QLabel(self.tab)
        self.labelAddress.setObjectName("labelAddress")
        self.verticalLayout_2.addWidget(self.labelAddress)
        self.Address = QtWidgets.QLineEdit(self.tab)
        self.Address.setMinimumSize(QtCore.QSize(0, 0))
        self.Address.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Address.setStatusTip("")
        self.Address.setStyleSheet("")
        self.Address.setClearButtonEnabled(True)
        self.Address.setObjectName("Address")
        self.verticalLayout_2.addWidget(self.Address)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelStartDate = QtWidgets.QLabel(self.tab)
        self.labelStartDate.setObjectName("labelStartDate")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelStartDate)
        self.StartDate = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartDate.sizePolicy().hasHeightForWidth())
        self.StartDate.setSizePolicy(sizePolicy)
        self.StartDate.setText("")
        self.StartDate.setObjectName("StartDate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.StartDate)
        self.horizontalLayout_6.addLayout(self.formLayout)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.labelEndDate = QtWidgets.QLabel(self.tab)
        self.labelEndDate.setObjectName("labelEndDate")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelEndDate)
        self.EndDate = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndDate.sizePolicy().hasHeightForWidth())
        self.EndDate.setSizePolicy(sizePolicy)
        self.EndDate.setObjectName("EndDate")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.EndDate)
        self.horizontalLayout_6.addLayout(self.formLayout_4)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.CreateCSV = QtWidgets.QPushButton(self.tab)
        self.CreateCSV.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateCSV.sizePolicy().hasHeightForWidth())
        self.CreateCSV.setSizePolicy(sizePolicy)
        self.CreateCSV.setObjectName("CreateCSV")
        self.verticalLayout_4.addWidget(self.CreateCSV)
        self.GetBalance = QtWidgets.QPushButton(self.tab)
        self.GetBalance.setEnabled(False)
        self.GetBalance.setObjectName("GetBalance")
        self.verticalLayout_4.addWidget(self.GetBalance)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.output = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setMinimumSize(QtCore.QSize(0, 150))
        self.output.setMaximumSize(QtCore.QSize(700, 16777215))
        self.output.setOpenExternalLinks(False)
        self.output.setOpenLinks(False)
        self.output.setObjectName("output")
        self.verticalLayout_3.addWidget(self.output)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelABAddress = QtWidgets.QLabel(self.tab_2)
        self.labelABAddress.setObjectName("labelABAddress")
        self.verticalLayout_9.addWidget(self.labelABAddress)
        self.ABAddress = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ABAddress.sizePolicy().hasHeightForWidth())
        self.ABAddress.setSizePolicy(sizePolicy)
        self.ABAddress.setMinimumSize(QtCore.QSize(0, 0))
        self.ABAddress.setStyleSheet("")
        self.ABAddress.setClearButtonEnabled(True)
        self.ABAddress.setObjectName("ABAddress")
        self.verticalLayout_9.addWidget(self.ABAddress)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelABNickname = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelABNickname.sizePolicy().hasHeightForWidth())
        self.labelABNickname.setSizePolicy(sizePolicy)
        self.labelABNickname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelABNickname.setObjectName("labelABNickname")
        self.verticalLayout_5.addWidget(self.labelABNickname)
        self.ABNickname = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ABNickname.sizePolicy().hasHeightForWidth())
        self.ABNickname.setSizePolicy(sizePolicy)
        self.ABNickname.setMinimumSize(QtCore.QSize(200, 0))
        self.ABNickname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ABNickname.setObjectName("ABNickname")
        self.verticalLayout_5.addWidget(self.ABNickname)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.addAddress = QtWidgets.QPushButton(self.tab_2)
        self.addAddress.setEnabled(False)
        self.addAddress.setObjectName("addAddress")
        self.horizontalLayout_2.addWidget(self.addAddress)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tableAddresses = QtWidgets.QTableView(self.tab_2)
        self.tableAddresses.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableAddresses.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableAddresses.setObjectName("tableAddresses")
        self.verticalLayout_10.addWidget(self.tableAddresses)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelSource = QtWidgets.QLabel(self.tab_3)
        self.labelSource.setObjectName("labelSource")
        self.verticalLayout_8.addWidget(self.labelSource)
        self.Source = QtWidgets.QLineEdit(self.tab_3)
        self.Source.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Source.setObjectName("Source")
        self.verticalLayout_8.addWidget(self.Source)
        self.labelMemo = QtWidgets.QLabel(self.tab_3)
        self.labelMemo.setObjectName("labelMemo")
        self.verticalLayout_8.addWidget(self.labelMemo)
        self.Memo = QtWidgets.QLineEdit(self.tab_3)
        self.Memo.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Memo.setObjectName("Memo")
        self.verticalLayout_8.addWidget(self.Memo)
        self.labelMinThresh = QtWidgets.QLabel(self.tab_3)
        self.labelMinThresh.setObjectName("labelMinThresh")
        self.verticalLayout_8.addWidget(self.labelMinThresh)
        self.MinThresh = QtWidgets.QLineEdit(self.tab_3)
        self.MinThresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.MinThresh.setObjectName("MinThresh")
        self.verticalLayout_8.addWidget(self.MinThresh)
        self.labelMaxThresh = QtWidgets.QLabel(self.tab_3)
        self.labelMaxThresh.setObjectName("labelMaxThresh")
        self.verticalLayout_8.addWidget(self.labelMaxThresh)
        self.MaxThresh = QtWidgets.QLineEdit(self.tab_3)
        self.MaxThresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.MaxThresh.setObjectName("MaxThresh")
        self.verticalLayout_8.addWidget(self.MaxThresh)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelCSVOutput = QtWidgets.QLabel(self.tab_3)
        self.labelCSVOutput.setObjectName("labelCSVOutput")
        self.verticalLayout_7.addWidget(self.labelCSVOutput)
        self.CSVOutputDest = QtWidgets.QLineEdit(self.tab_3)
        self.CSVOutputDest.setMinimumSize(QtCore.QSize(300, 0))
        self.CSVOutputDest.setMaximumSize(QtCore.QSize(450, 16777215))
        self.CSVOutputDest.setObjectName("CSVOutputDest")
        self.verticalLayout_7.addWidget(self.CSVOutputDest)
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.folderButton = QtWidgets.QPushButton(self.tab_3)
        self.folderButton.setObjectName("folderButton")
        self.horizontalLayout_4.addWidget(self.folderButton)
        self.openFolderButton = QtWidgets.QPushButton(self.tab_3)
        self.openFolderButton.setObjectName("openFolderButton")
        self.horizontalLayout_4.addWidget(self.openFolderButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelTheme = QtWidgets.QLabel(self.tab_3)
        self.labelTheme.setObjectName("labelTheme")
        self.verticalLayout_6.addWidget(self.labelTheme)
        self.radioButtonLightMode = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonLightMode.setObjectName("radioButtonLightMode")
        self.verticalLayout_6.addWidget(self.radioButtonLightMode)
        self.radioButtonDarkMode = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonDarkMode.setObjectName("radioButtonDarkMode")
        self.verticalLayout_6.addWidget(self.radioButtonDarkMode)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        spacerItem6 = QtWidgets.QSpacerItem(40, 194, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SaveSettings = QtWidgets.QPushButton(self.tab_3)
        self.SaveSettings.setObjectName("SaveSettings")
        self.horizontalLayout_3.addWidget(self.SaveSettings)
        self.resetButton = QtWidgets.QPushButton(self.tab_3)
        self.resetButton.setToolTip("")
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_3.addWidget(self.resetButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_14.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem11)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
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
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionOpen_Log = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log.setObjectName("actionOpen_Log")
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionOpen_Log)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_updates)
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
        MainWindow.setTabOrder(self.output, self.ABAddress)
        MainWindow.setTabOrder(self.ABAddress, self.ABNickname)
        MainWindow.setTabOrder(self.ABNickname, self.addAddress)
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
        self.labelAddress.setText(QtWidgets.QApplication.translate("MainWindow", "Stellar Address", None, -1))
        self.Address.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Stellar Address (required): A Stellar address to receive transactions from", None, -1))
        self.labelStartDate.setText(QtWidgets.QApplication.translate("MainWindow", "Start Date", None, -1))
        self.StartDate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Start Date (required): The date of the oldest transaction received", None, -1))
        self.StartDate.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "YYYY-MM-DD", None, -1))
        self.labelEndDate.setText(QtWidgets.QApplication.translate("MainWindow", "End Date", None, -1))
        self.EndDate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "End Date (optional): Create a range of transactions received with a specific end date", None, -1))
        self.EndDate.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "YYYY-MM-DD", None, -1))
        self.CreateCSV.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create CSV file with chosen parameters", None, -1))
        self.CreateCSV.setText(QtWidgets.QApplication.translate("MainWindow", "Create CSV", None, -1))
        self.GetBalance.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Print the balance", None, -1))
        self.GetBalance.setText(QtWidgets.QApplication.translate("MainWindow", "Get Balance", None, -1))
        self.output.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Information</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Stellar Address</span> (required): A Stellar address to receive transactions from</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Start Date</span> (required): The date of the oldest transaction received</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">End Date</span> (optional): Create a range of transactions received with a specific end date</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______________________________________________________________________</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Main", None, -1))
        self.labelABAddress.setText(QtWidgets.QApplication.translate("MainWindow", "Stellar Address", None, -1))
        self.ABAddress.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Stellar address (required)", None, -1))
        self.labelABNickname.setText(QtWidgets.QApplication.translate("MainWindow", "Nickname (optional)", None, -1))
        self.ABNickname.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Nickname (optional)", None, -1))
        self.addAddress.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add to address book", None, -1))
        self.addAddress.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Address Book", None, -1))
        self.labelSource.setText(QtWidgets.QApplication.translate("MainWindow", "Source", None, -1))
        self.labelMemo.setText(QtWidgets.QApplication.translate("MainWindow", "Memo", None, -1))
        self.labelMinThresh.setText(QtWidgets.QApplication.translate("MainWindow", "Minimum Threshold", None, -1))
        self.labelMaxThresh.setText(QtWidgets.QApplication.translate("MainWindow", "Maximum Threshold", None, -1))
        self.labelCSVOutput.setText(QtWidgets.QApplication.translate("MainWindow", "CSV Output Destination", None, -1))
        self.folderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Folder", None, -1))
        self.openFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Open Folder", None, -1))
        self.labelTheme.setText(QtWidgets.QApplication.translate("MainWindow", "Theme", None, -1))
        self.radioButtonLightMode.setText(QtWidgets.QApplication.translate("MainWindow", "Light", None, -1))
        self.radioButtonDarkMode.setText(QtWidgets.QApplication.translate("MainWindow", "Dark", None, -1))
        self.SaveSettings.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save chosen settings", None, -1))
        self.SaveSettings.setText(QtWidgets.QApplication.translate("MainWindow", "Save Settings", None, -1))
        self.resetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionCheck_for_updates.setText(QtWidgets.QApplication.translate("MainWindow", "Check for updates", None, -1))
        self.actionSave_Settings.setText(QtWidgets.QApplication.translate("MainWindow", "Save Settings", None, -1))
        self.actionSave_Settings.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionOpen_Log.setText(QtWidgets.QApplication.translate("MainWindow", "Open Log", None, -1))

