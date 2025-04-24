#my code
import menu
import sqlite3
from PyQt5.QtWidgets import *
#--------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form9(object):
    def setupUi(self, form9):
        form9.setObjectName("form9")
        form9.resize(1456, 997)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form9)
        self.frame.setMinimumSize(QtCore.QSize(900, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(140, 60, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.frame)
        self.l2.setGeometry(QtCore.QRect(90, 130, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.frame)
        self.l3.setGeometry(QtCore.QRect(50, 270, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLabel(self.frame)
        self.l4.setGeometry(QtCore.QRect(60, 350, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setObjectName("l4")
        self.le1 = QtWidgets.QLineEdit(self.frame)
        self.le1.setGeometry(QtCore.QRect(360, 270, 341, 41))
        self.le1.setObjectName("le1")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)
        self.le1.setFont(font)
        self.le2 = QtWidgets.QLineEdit(self.frame)
        self.le2.setGeometry(QtCore.QRect(360, 350, 341, 41))
        self.le2.setObjectName("le2")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)
        self.le2.setFont(font)
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(750, 260, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.tw1 = QtWidgets.QTableWidget(self.frame)
        self.tw1.setGeometry(QtCore.QRect(60, 450, 781, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tw1.setFont(font)
        self.tw1.setStyleSheet("QHeaderView::section {\n"
"    background-color: #d3d3d3; /* Light gray or choose any */\n"
"    color: black;              /* Optional: Text color */\n"
"    font-weight: bold;  \n"
"    font-size: 15px;\n"
"    font-family: times new roman;       /* Optional: Make header text bold */\n"
"}\n"
"QTableWidget {\n"
"    background-color: #e6f7ff;\n"
"}")
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
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(360, 880, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form9)
        QtCore.QMetaObject.connectSlotsByName(form9)
        #my work
        self.tw1.verticalHeader().setVisible(False)
        self.tw1.setColumnWidth(0, 180);
        self.tw1.setColumnWidth(1, 180);
        self.tw1.setColumnWidth(2, 240);
        self.tw1.setColumnWidth(3, 180);
        self.form9=form9
        self.b1.clicked.connect(self.find)
        self.b2.clicked.connect(self.back)

    def find(self):
        db=sqlite3.connect("bank.db")
        a=self.le1.text()
        b="select * from customer where accno="+a+";"
        r=db.execute(b)
        rec=r.fetchall()
        db.close()
        if len(rec)==0:
            QMessageBox.critical(self.form9, "ERROR","INVALID ACCOUNT NUMBER")
            self.le1.clear()
            self.le2.clear()
        else:
            self.le2.setText(str(rec[0][1]))
            db=sqlite3.connect("bank.db")
            a="select tid,dot,ttype,tamount from trans where accno="+a+""
            r=db.execute(a)
            self.tw1.setRowCount(0)
            for rowno, rec in enumerate(r):
                self.tw1.insertRow(rowno)
                for columnno, data in enumerate(rec):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tw1.setItem(rowno, columnno, item)
            db.close()

    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_form2()
        self.ui.setupUi(self.form2)
        self.form9.close()
        self.form2.showMaximized()

    def retranslateUi(self, form9):
        _translate = QtCore.QCoreApplication.translate
        form9.setWindowTitle(_translate("form9", "CUSTOMER TRANSACTION"))
        self.l1.setText(_translate("form9", "INDIAN BANK"))
        self.l2.setText(_translate("form9", "FETCH TRANSACTION DETAILS"))
        self.l3.setText(_translate("form9", "ACCOUNT NUMBER"))
        self.l4.setText(_translate("form9", "CUSTOMER NAME"))
        self.b1.setText(_translate("form9", "FIND"))
        item = self.tw1.horizontalHeaderItem(0)
        item.setText(_translate("form9", "ID"))
        item = self.tw1.horizontalHeaderItem(1)
        item.setText(_translate("form9", "DATE"))
        item = self.tw1.horizontalHeaderItem(2)
        item.setText(_translate("form9", "TRANS MODE"))
        item = self.tw1.horizontalHeaderItem(3)
        item.setText(_translate("form9", "AMOUNT"))
        self.b2.setText(_translate("form9", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form9 = QtWidgets.QWidget()
    ui = Ui_form9()
    ui.setupUi(form9)
    form9.show()
    sys.exit(app.exec_())
