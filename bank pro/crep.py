#my code
import menu
import sqlite3
from PyQt5.QtWidgets import *
#-----------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form6(object):
    def setupUi(self, form6):
        form6.setObjectName("form6")
        form6.resize(1396, 936)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        form6.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.frame = QtWidgets.QFrame(form6)
        self.frame.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.tw1 = QtWidgets.QTableWidget(self.frame)
        self.tw1.setGeometry(QtCore.QRect(-10, 70, 701, 761))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.tw1.setFont(font)
        self.tw1.setStyleSheet(
            "QHeaderView::section {\n"
            "    background-color: #d3d3d3;\n"
            "    color: black;\n"
            "    font-weight: bold;\n"
            "    font-size: 18px;\n"
            "    font-family: times new roman;\n"
            "}\n"
            "QTableWidget {\n"
            "    background-color: #e6f7ff;\n"
            "}"
        )
        self.tw1.setObjectName("tw1")
        self.tw1.setColumnCount(5)
        self.tw1.setRowCount(0)

        item = QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tw1.setHorizontalHeaderItem(4, item)

        self.b1 = QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(250, 880, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")

        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form6)
        QtCore.QMetaObject.connectSlotsByName(form6)
        # my code
        self.form6 = form6
        self.b1.clicked.connect(self.back)
        db = sqlite3.connect("bank.db")
        a = "select * from customer"
        r = db.execute(a)
        self.tw1.setRowCount(0)
        for rowno, rec in enumerate(r):
            self.tw1.insertRow(rowno)
            for columnno, data in enumerate(rec):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tw1.setItem(rowno, columnno, item)
        db.close()
        self.tw1.verticalHeader().setVisible(False)
        self.tw1.setColumnWidth(0, 100)  # ACC NO
        self.tw1.setColumnWidth(1, 200)  # NAME
        self.tw1.setColumnWidth(2, 250)  # ADDRESS
        self.tw1.setColumnWidth(3, 150)  # PHN NO
        self.tw1.setColumnWidth(4, 180)  # BALANCE
    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_form2()
        self.ui.setupUi(self.form2)
        self.form6.close()
        self.form2.show()

    def retranslateUi(self, form6):
        _translate = QtCore.QCoreApplication.translate
        form6.setWindowTitle(_translate("form6", "CUSTOMER REPORT"))
        self.frame.setStyleSheet(_translate("form6",
            "QHeaderView::section {\n"
            "    background-color: #d3d3d3;\n"
            "    color: black;\n"
            "    font-weight: bold;\n"
            "    font-size: 18px;\n"
            "    font-family: times new roman;\n"
            "}\n"
            "QTableWidget {\n"
            "    background-color: #e6f7ff;\n"
            "}"
        ))
        item = self.tw1.horizontalHeaderItem(0)
        item.setText(_translate("form6", "ACC NO"))
        item = self.tw1.horizontalHeaderItem(1)
        item.setText(_translate("form6", "NAME"))
        item = self.tw1.horizontalHeaderItem(2)
        item.setText(_translate("form6", "ADDRESS"))
        item = self.tw1.horizontalHeaderItem(3)
        item.setText(_translate("form6", "PHN NO"))
        item = self.tw1.horizontalHeaderItem(4)
        item.setText(_translate("form6", "BALANCE"))
        self.b1.setText(_translate("form6", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form6 = QtWidgets.QWidget()
    ui = Ui_form6()
    ui.setupUi(form6)
    form6.showMaximized()
    sys.exit(app.exec_())
