#my work 1
import sqlite3
from PyQt5.QtWidgets import *
#------------


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form2(object):
    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(636, 503)
        self.l1 = QtWidgets.QLabel(form2)
        self.l1.setGeometry(QtCore.QRect(160, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.le1 = QtWidgets.QLineEdit(form2)
        self.le1.setGeometry(QtCore.QRect(250, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le1.setFont(font)
        self.le1.setObjectName("le1")
        self.b1 = QtWidgets.QPushButton(form2)
        self.b1.setGeometry(QtCore.QRect(390, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.l2 = QtWidgets.QLabel(form2)
        self.l2.setGeometry(QtCore.QRect(160, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.le2 = QtWidgets.QLineEdit(form2)
        self.le2.setGeometry(QtCore.QRect(250, 120, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le2.setFont(font)
        self.le2.setObjectName("le2")
        self.l3 = QtWidgets.QLabel(form2)
        self.l3.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.le3 = QtWidgets.QLineEdit(form2)
        self.le3.setGeometry(QtCore.QRect(250, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le3.setFont(font)
        self.le3.setObjectName("le3")
        self.l4 = QtWidgets.QLabel(form2)
        self.l4.setGeometry(QtCore.QRect(160, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.le4 = QtWidgets.QLineEdit(form2)
        self.le4.setGeometry(QtCore.QRect(250, 240, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le4.setFont(font)
        self.le4.setObjectName("le4")
        self.b2 = QtWidgets.QPushButton(form2)
        self.b2.setGeometry(QtCore.QRect(160, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(form2)
        self.b3.setGeometry(QtCore.QRect(320, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(form2)
        self.b4.setGeometry(QtCore.QRect(160, 390, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")

        self.retranslateUi(form2)
        QtCore.QMetaObject.connectSlotsByName(form2)
        #my work
        self.form2=form2
        self.b1.clicked.connect(self.findfn)
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        self.b2.clicked.connect(self.delfn)
        self.b3.clicked.connect(self.updatefn)

    def findfn(self):
        a=self.le1.text()
        db=sqlite3.connect("mydb.db")
        #select * from emp where eid=7
        s="select * from emp where eid="+a+""
        r=db.execute(s)
        #print(r)
        rec=r.fetchall()
        db.close()
        #print(rec)
        #print(rec[0])
        #print(rec[0][0])            #eid
        #print(rec[0][1])            #name
        #print(rec[0][2])            #age
        #print(rec[0][3])            #phone

        if len(rec)==0:
            self.le2.clear()
            self.le3.clear()
            self.le4.clear()
            self.b2.setEnabled(False)
            self.b3.setEnabled(False)
            QMessageBox.about(self.form2,"Invalid ID","No record for the given ID")
        else:
            self.le2.setText( str(rec[0][1]) )    #name on le2
            self.le3.setText( str(rec[0][2]) )    #age on le3
            self.le4.setText( str(rec[0][3]) )    #phone on le4
            self.b2.setEnabled(True)
            self.b3.setEnabled(True)

    def delfn(self):
        a=self.le1.text()
        db=sqlite3.connect("mydb.db")
        #delete from emp where eid=3;
        s="delete from emp where eid="+a+";"
        db.execute(s)
        db.commit()
        db.close()
        self.le1.clear()
        self.le2.clear()
        self.le3.clear()
        self.le4.clear()
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        QMessageBox.about(self.form2,"DELETE","Record deleted sucessfully")

    def updatefn(self):
        a=self.le1.text()
        b=self.le2.text()
        c=self.le3.text()
        d=self.le4.text()
        db=sqlite3.connect("mydb.db")
        #update emp set name='navin',age=55,phone=000000 where eid=8;
        s="update emp set name='"+b+"',age="+c+",phone="+d+" where eid="+a+";"
        db.execute(s)
        db.commit()
        db.close()
        QMessageBox.about(self.form2,"UPDATE","Record updated sucessfully")
        self.le1.clear()
        self.le2.clear()
        self.le3.clear()
        self.le4.clear()
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        
        

        

    def retranslateUi(self, form2):
        _translate = QtCore.QCoreApplication.translate
        form2.setWindowTitle(_translate("form2", "UPDATE"))
        self.l1.setText(_translate("form2", "Enter ID:"))
        self.b1.setText(_translate("form2", "FIND"))
        self.l2.setText(_translate("form2", "Name:"))
        self.l3.setText(_translate("form2", "Age:"))
        self.l4.setText(_translate("form2", "Phone:"))
        self.b2.setText(_translate("form2", "DELETE"))
        self.b3.setText(_translate("form2", "UPDATE"))
        self.b4.setText(_translate("form2", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form2 = QtWidgets.QWidget()
    ui = Ui_form2()
    ui.setupUi(form2)
    form2.show()
    sys.exit(app.exec_())
