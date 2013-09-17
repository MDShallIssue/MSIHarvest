# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 658)
        # MainWindow.showFullScreen()
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 391, 151))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText("")
        # pixmap = QtGui.QPixmap("Resources/MSI_Logo_Header-612x121.png")
        # self.label_4.setPixmap(pixmap)
        self.label_4.setPixmap(QtGui.QPixmap("MSI_Logo_Header-612x121.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(410, 70, 541, 410))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.emailEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.emailEntry.setMinimumSize(QtCore.QSize(0, 70))
        self.emailEntry.setMaximumSize(QtCore.QSize(500, 70))
        self.emailEntry.setBaseSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.emailEntry.setFont(font)
        self.emailEntry.setObjectName("emailEntry")
        self.gridLayout_3.addWidget(self.emailEntry, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 15, 0, 1, 1)
        self.firstNameEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.firstNameEntry.setMinimumSize(QtCore.QSize(0, 70))
        self.firstNameEntry.setMaximumSize(QtCore.QSize(250, 70))
        self.firstNameEntry.setBaseSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.firstNameEntry.setFont(font)
        self.firstNameEntry.setObjectName("firstNameEntry")
        self.gridLayout_3.addWidget(self.firstNameEntry, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lastNameEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lastNameEntry.setMinimumSize(QtCore.QSize(250, 70))
        self.lastNameEntry.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lastNameEntry.setBaseSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lastNameEntry.setFont(font)
        self.lastNameEntry.setObjectName("lastNameEntry")
        self.gridLayout_3.addWidget(self.lastNameEntry, 6, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 7, 0, 1, 1)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.gridLayoutWidget_2)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(800, 60))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(800, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout_3.addWidget(self.commandLinkButton, 14, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1050, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MSI", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Email Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("MainWindow", "Allow MSI to Send Me Further Information", None, QtGui.QApplication.UnicodeUTF8))

    def save_record(self, parent=None):
        with open("msi.txt", "a") as outfile:
            outfile.write('"%s","%s","%s"\r\n' % (self.emailEntry.text(), self.firstNameEntry.text(), self.lastNameEntry.text()))
            print "Output written"

        self.emailEntry.setText("")
        self.firstNameEntry.setText("")
        self.lastNameEntry.setText("")
        self.emailEntry.setFocus()

        text = "Thank you for helping defend the rights of all Marylanders."
        thanks = QtGui.QMessageBox()
        thanks.setText(text)
        thanks.exec_()
            

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            if QtGui.QWidget.hasFocus(self.emailEntry):
                self.firstNameEntry.setFocus()
            elif QtGui.QWidget.hasFocus(self.firstNameEntry):
                self.lastNameEntry.setFocus()
            elif QtGui.QWidget.hasFocus(self.lastNameEntry):
                self.save_record()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.save_record)

# import MSIResources_rc

class ControlMainWindow(QtGui.QMainWindow):
    def hello(self, parent=None):
        # super(ControlMainWindow, self).__init__(parent)
        print "Hello!"

    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui =  MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    # mySW = ControlMainWindow()
    # mySW.show()
    sys.exit(app.exec_())

