#my code
import menu
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form10(object):
    def setupUi(self, form10):
        form10.setObjectName("form10")
        form10.resize(1405, 959)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form10)
        self.frame.setMinimumSize(QtCore.QSize(900, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(80, 40, 711, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.frame)
        self.l2.setGeometry(QtCore.QRect(80, 120, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.frame)
        self.l3.setGeometry(QtCore.QRect(20, 250, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.de1 = QtWidgets.QDateEdit(self.frame)
        self.de1.setGeometry(QtCore.QRect(300, 250, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.de1.setFont(font)
        self.de1.setDate(QtCore.QDate(2025, 4, 13))
        self.de1.setObjectName("de1")
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(640, 250, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.tw1 = QtWidgets.QTableWidget(self.frame)
        self.tw1.setGeometry(QtCore.QRect(60, 380, 781, 451))
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
"    font-size: 20px;\n"
"    font-family: times new roman;       /* Optional: Make header text bold */\n"
"}\n"
"QTableWidget {\n"
"    background-color: #e6f7ff;\n"
"}")
        self.tw1.setObjectName("tw1")
        self.tw1.setColumnCount(6)
        self.tw1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(5, item)
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(390, 880, 97, 44))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form10)
        QtCore.QMetaObject.connectSlotsByName(form10)
        #my code
        cd=QDate.currentDate()
        self.de1.setDate(cd)
        self.tw1.verticalHeader().setVisible(False)
        self.tw1.setColumnWidth(0, 80);
        self.tw1.setColumnWidth(1, 140);
        self.tw1.setColumnWidth(2, 135);
        self.tw1.setColumnWidth(3, 135);
        self.tw1.setColumnWidth(4, 150);
        self.tw1.setColumnWidth(5, 145);
        self.form10=form10
        self.b1.clicked.connect(self.show)
        self.b2.clicked.connect(self.back)
        
    def show(self):
        db=sqlite3.connect("bank.db")
        a=self.de1.date().toString("dd/MM/yyyy")
        b="select * from trans where dot='"+a+"';"
        r=db.execute(b)
        rec=r.fetchall()
        if len(rec)==0:
            self.tw1.setRowCount(0)
            QMessageBox.critical(self.form10, "ERROR","NO ENTRIES FOUND FOR THE CHOSEN DATE")
        else:
            self.tw1.setRowCount(0)
            for rowno,rec1 in enumerate(rec):
                self.tw1.insertRow(rowno)
                for columnno,data in enumerate(rec1):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tw1.setItem(rowno, columnno, item) 
        db.close()

    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_form2()
        self.ui.setupUi(self.form2)
        self.form10.close()
        self.form2.showMaximized()

    def retranslateUi(self, form10):
        _translate = QtCore.QCoreApplication.translate
        form10.setWindowTitle(_translate("form10", "RETRIEVE TRANSACTIONS"))
        self.l1.setText(_translate("form10", "INDIAN BANK"))
        self.l2.setText(_translate("form10", "RETRIEVE TRANSACTION HISTORY"))
        self.l3.setText(_translate("form10", "SELECT DATE"))
        self.b1.setText(_translate("form10", "SHOW"))
        item = self.tw1.horizontalHeaderItem(0)
        item.setText(_translate("form10", "ID"))
        item = self.tw1.horizontalHeaderItem(1)
        item.setText(_translate("form10", "ACC NO"))
        item = self.tw1.horizontalHeaderItem(2)
        item.setText(_translate("form10", "NAME"))
        item = self.tw1.horizontalHeaderItem(3)
        item.setText(_translate("form10", "DATE"))
        item = self.tw1.horizontalHeaderItem(4)
        item.setText(_translate("form10", "TRANS MODE"))
        item = self.tw1.horizontalHeaderItem(5)
        item.setText(_translate("form10", "AMOUNT"))
        self.b2.setText(_translate("form10", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form10 = QtWidgets.QWidget()
    ui = Ui_form10()
    ui.setupUi(form10)
    form10.show()
    sys.exit(app.exec_())
