#my code
import sqlite3
from PyQt5.QtWidgets import *
#-------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form3(object):
    def setupUi(self, form3):
        form3.setObjectName("form3")
        form3.resize(793, 654)
        self.tw1 = QtWidgets.QTableWidget(form3)
        self.tw1.setGeometry(QtCore.QRect(30, 20, 731, 571))
        self.tw1.setObjectName("tw1")
        self.tw1.setColumnCount(4)
        self.tw1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(3, item)
        self.b1 = QtWidgets.QPushButton(form3)
        self.b1.setGeometry(QtCore.QRect(340, 600, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")

        self.retranslateUi(form3)
        QtCore.QMetaObject.connectSlotsByName(form3)
        #my code
        db=sqlite3.connect("mydb.db")
        #select * from Emp;
        s="select * from Emp;"
        r=db.execute(s)

        self.tw1.setRowCount(0) #clear the table widget
        for rowno,rec in enumerate(r):
            self.tw1.insertRow(rowno)
            for columnno,data in enumerate(rec):
                self.tw1.setItem(rowno,columnno,QTableWidgetItem(str(data)))
        db.close()
        self.tw1.verticalHeader().setVisible(False)
        st="::section{background-color:lightblue;}"
        self.tw1.horizontalHeader().setStyleSheet(st)
                
    def retranslateUi(self, form3):
        _translate = QtCore.QCoreApplication.translate
        form3.setWindowTitle(_translate("form3", "EMPLOYEE LIST"))
        item = self.tw1.horizontalHeaderItem(0)
        item.setText(_translate("form3", "ID"))
        item = self.tw1.horizontalHeaderItem(1)
        item.setText(_translate("form3", "NAME"))
        item = self.tw1.horizontalHeaderItem(2)
        item.setText(_translate("form3", "AGE"))
        item = self.tw1.horizontalHeaderItem(3)
        item.setText(_translate("form3", "PHONE NO"))
        self.b1.setText(_translate("form3", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form3 = QtWidgets.QWidget()
    ui = Ui_form3()
    ui.setupUi(form3)
    form3.show()
    sys.exit(app.exec_())
