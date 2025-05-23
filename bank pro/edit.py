#my code
import sqlite3
from PyQt5.QtWidgets import *
import menu
#--------------------------------#
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form4(object):
    def setupUi(self, form4):
        form4.setObjectName("form4")
        form4.resize(1353, 858)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form4)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(80, 100, 551, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.frame)
        self.l2.setGeometry(QtCore.QRect(30, 240, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.le1 = QtWidgets.QLineEdit(self.frame)
        self.le1.setGeometry(QtCore.QRect(270, 240, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le1.setFont(font)
        self.le1.setObjectName("le1")
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(550, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.l3 = QtWidgets.QLabel(self.frame)
        self.l3.setGeometry(QtCore.QRect(30, 310, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLabel(self.frame)
        self.l4.setGeometry(QtCore.QRect(20, 380, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setObjectName("l4")
        self.le2 = QtWidgets.QLineEdit(self.frame)
        self.le2.setGeometry(QtCore.QRect(270, 310, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le2.setFont(font)
        self.le2.setObjectName("le2")
        self.le3 = QtWidgets.QLineEdit(self.frame)
        self.le3.setGeometry(QtCore.QRect(270, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le3.setFont(font)
        self.le3.setObjectName("le3")
        self.l5 = QtWidgets.QLabel(self.frame)
        self.l5.setGeometry(QtCore.QRect(30, 450, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setObjectName("l5")
        self.le4 = QtWidgets.QLineEdit(self.frame)
        self.le4.setGeometry(QtCore.QRect(270, 450, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le4.setFont(font)
        self.le4.setObjectName("le4")
        self.l6 = QtWidgets.QLabel(self.frame)
        self.l6.setGeometry(QtCore.QRect(30, 520, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setAlignment(QtCore.Qt.AlignCenter)
        self.l6.setObjectName("l6")
        self.le5 = QtWidgets.QLineEdit(self.frame)
        self.le5.setGeometry(QtCore.QRect(270, 520, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.le5.setFont(font)
        self.le5.setObjectName("le5")
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(130, 610, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.frame)
        self.b3.setGeometry(QtCore.QRect(380, 610, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.frame)
        self.b4.setGeometry(QtCore.QRect(150, 710, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form4)
        QtCore.QMetaObject.connectSlotsByName(form4)
        #my code
        self.form4=form4
        self.b1.clicked.connect(self.find)
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        self.b2.clicked.connect(self.delete)
        self.b3.clicked.connect(self.update)
        self.b4.clicked.connect(self.back)
        
       

    def find(self):
        a=self.le1.text()
        db=sqlite3.connect("bank.db")
        s="select * from customer where accno="+a+";"
        r=db.execute(s)
        rec=r.fetchall()
        db.close()

        if len(rec)==0:
            self.le2.clear()
            self.le3.clear()
            self.le4.clear()
            self.le5.clear()
            self.b2.setEnabled(False)
            self.b3.setEnabled(False)
            QMessageBox.about(self.form4,"Invalid Id","Not record found")

        else:
            self.le2.setText( str(rec[0][1]) )  
            self.le3.setText( str(rec[0][2]) )
            self.le4.setText( str(rec[0][3]) )
            self.le5.setText( str(rec[0][4]) )
            self.b2.setEnabled(True)
            self.b3.setEnabled(True)

    def delete(self):
        a=self.le1.text()
        db=sqlite3.connect("bank.db")
        s="delete from customer where accno="+a+";"
        db.execute(s)
        db.commit()
        db.close()
        self.le1.clear()
        self.le2.clear()
        self.le3.clear()
        self.le4.clear()
        self.le5.clear()
        QMessageBox.about(self.form4,"DELETE","Customer account deleted successfully")
        

    def update(self):
        a=self.le1.text()
        b=self.le2.text()
        c=self.le3.text()
        d=self.le4.text()
        e=self.le5.text()
        db=sqlite3.connect("bank.db")
        s="UPDATE customer set name='"+b+"',address='"+c+"', phone="+d+",balance="+e+" where accno="+a+";"
        
        db.execute(s)
        db.commit()
        db.close()
        QMessageBox.about(self.form4,"UPDATE","Customer account updated")
        a=self.le1.clear()
        b=self.le2.clear()
        c=self.le3.clear()
        d=self.le4.clear()
        e=self.le5.clear()
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)

    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_form2()
        self.ui.setupUi(self.form2)
        self.form4.close()
        self.form2.show()
    

    def retranslateUi(self, form4):
        _translate = QtCore.QCoreApplication.translate
        form4.setWindowTitle(_translate("form4", "EDIT CUSTOMER"))
        self.l1.setText(_translate("form4", "CUSTOMER EDIT OF INDIAN BANK"))
        self.l2.setText(_translate("form4", "ACCOUNT NUMBER"))
        self.b1.setText(_translate("form4", "FIND"))
        self.l3.setText(_translate("form4", "ACC HOLDER NAME"))
        self.l4.setText(_translate("form4", "RESEDENTIAL ADDRESS"))
        self.l5.setText(_translate("form4", "      PHONE NUMBER"))
        self.l6.setText(_translate("form4", "ACCOUNT BALANCE"))
        self.b2.setText(_translate("form4", "DELETE"))
        self.b3.setText(_translate("form4", "UPDATE"))
        self.b4.setText(_translate("form4", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form4 = QtWidgets.QWidget()
    ui = Ui_form4()
    ui.setupUi(form4)
    form4.showMaximized()
    sys.exit(app.exec_())
