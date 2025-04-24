#my work 1
import sys
#---------------


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form1(object):
    def setupUi(self, form1):
        form1.setObjectName("form1")
        form1.resize(629, 483)
        self.centralwidget = QtWidgets.QWidget(form1)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(100, 160, 431, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l1.setFont(font)
        self.l1.setText("")
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        form1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        self.menubar.setObjectName("menubar")
        self.menuMy_Details = QtWidgets.QMenu(self.menubar)
        self.menuMy_Details.setObjectName("menuMy_Details")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        form1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form1)
        self.statusbar.setObjectName("statusbar")
        form1.setStatusBar(self.statusbar)
        self.miname = QtWidgets.QAction(form1)
        self.miname.setObjectName("miname")
        self.miage = QtWidgets.QAction(form1)
        self.miage.setObjectName("miage")
        self.mifn = QtWidgets.QAction(form1)
        self.mifn.setObjectName("mifn")
        self.miexit = QtWidgets.QAction(form1)
        self.miexit.setObjectName("miexit")
        self.mired = QtWidgets.QAction(form1)
        self.mired.setObjectName("mired")
        self.miblue = QtWidgets.QAction(form1)
        self.miblue.setObjectName("miblue")
        self.miblack = QtWidgets.QAction(form1)
        self.miblack.setObjectName("miblack")
        self.menuMy_Details.addAction(self.miname)
        self.menuMy_Details.addAction(self.miage)
        self.menuMy_Details.addAction(self.mifn)
        self.menuMy_Details.addSeparator()
        self.menuMy_Details.addAction(self.miexit)
        self.menuColor.addAction(self.mired)
        self.menuColor.addAction(self.miblue)
        self.menuColor.addAction(self.miblack)
        self.menubar.addAction(self.menuMy_Details.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())

        self.retranslateUi(form1)
        QtCore.QMetaObject.connectSlotsByName(form1)
        #my work
        self.miname.triggered.connect(self.fn1)
        self.miage.triggered.connect(self.fn2)
        self.mifn.triggered.connect(self.fn3)
        self.miexit.triggered.connect(self.fn4)
        self.mired.triggered.connect(self.fn5)
        self.miblue.triggered.connect(self.fn6)
        self.miblack.triggered.connect(self.fn7)
        

    def fn1(self):
        self.l1.setText("GAYATHRI PRASAD")

    def fn2(self):
        self.l1.setText("17")

    def fn3(self):
        self.l1.setText("NEELAKANDA PRASAD")

    def fn4(self):
        sys.exit()

    def fn5(self):
        self.l1.setStyleSheet("color:RED;")

    def fn6(self):
        self.l1.setStyleSheet("color:BLUE;")

    def fn7(self):
        self.l1.setStyleSheet("color:BLACK;")

    

    def retranslateUi(self, form1):
        _translate = QtCore.QCoreApplication.translate
        form1.setWindowTitle(_translate("form1", "MENU DEMO"))
        self.menuMy_Details.setTitle(_translate("form1", "My Details"))
        self.menuColor.setTitle(_translate("form1", "Color"))
        self.miname.setText(_translate("form1", "Name"))
        self.miname.setShortcut(_translate("form1", "Ctrl+N"))
        self.miage.setText(_translate("form1", "Age"))
        self.miage.setShortcut(_translate("form1", "Ctrl+A"))
        self.mifn.setText(_translate("form1", "Father Name"))
        self.miexit.setText(_translate("form1", "Exit"))
        self.mired.setText(_translate("form1", "Red"))
        self.mired.setShortcut(_translate("form1", "Ctrl+R"))
        self.miblue.setText(_translate("form1", "Blue"))
        self.miblue.setShortcut(_translate("form1", "Ctrl+B"))
        self.miblack.setText(_translate("form1", "Black"))
        self.miblack.setShortcut(_translate("form1", "Ctrl+L"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QMainWindow()
    ui = Ui_form1()
    ui.setupUi(form1)
    form1.show()
    sys.exit(app.exec_())
