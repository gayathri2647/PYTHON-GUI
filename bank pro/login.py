#my code
import menu
from PyQt5.QtWidgets import *
#---------------------------------#
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form1(object):
    def setupUi(self, form1):
        form1.setObjectName("form1")
        form1.resize(1392, 854)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form1)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(70, 100, 571, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.frame)
        self.l2.setGeometry(QtCore.QRect(80, 300, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.le1 = QtWidgets.QLineEdit(self.frame)
        self.le1.setGeometry(QtCore.QRect(330, 300, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le1.setFont(font)
        self.le1.setObjectName("le1")
        self.l3 = QtWidgets.QLabel(self.frame)
        self.l3.setGeometry(QtCore.QRect(90, 420, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.le2 = QtWidgets.QLineEdit(self.frame)
        self.le2.setGeometry(QtCore.QRect(330, 410, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le2.setFont(font)
        self.le2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le2.setObjectName("le2")
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(230, 600, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form1)
        QtCore.QMetaObject.connectSlotsByName(form1)
        #my code
        self.b1.clicked.connect(self.login)
        self.form1=form1
        

    def login(self):
        a=self.le1.text()
        b=self.le2.text()
        if a=="GAYATHRI" and b=="GAYU2647":
            self.form2 = QtWidgets.QWidget()
            self.ui = menu.Ui_form2()
            self.ui.setupUi(self.form2)
            self.form1.close()
            self.form2.showMaximized()
        else:
            QMessageBox.critical(self.form1,"ERROR","Invalid Username or Password")

    def retranslateUi(self, form1):
        _translate = QtCore.QCoreApplication.translate
        form1.setWindowTitle(_translate("form1", "LOGIN"))
        self.l1.setText(_translate("form1", "INDIAN BANK"))
        self.l2.setText(_translate("form1", "Employee ID"))
        self.l3.setText(_translate("form1", "Password "))
        self.b1.setText(_translate("form1", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QWidget()
    ui = Ui_form1()
    ui.setupUi(form1)
    form1.showMaximized()
    sys.exit(app.exec_())
