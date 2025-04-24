#my code
import sqlite3
from PyQt5.QtWidgets import *
import menu
#------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form7(object):
    def setupUi(self, form7):
        form7.setObjectName("form7")
        form7.resize(1498, 945)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        form7.setFont(font)

        self.horizontalLayout = QtWidgets.QHBoxLayout(form7)
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.frame = QtWidgets.QFrame(form7)
        self.frame.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.tw1 = QtWidgets.QTableWidget(self.frame)
        self.tw1.setGeometry(QtCore.QRect(-10, 70, 701, 761))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.tw1.setFont(font)

        self.tw1.setStyleSheet("""
QHeaderView::section {
    background-color: #d3d3d3;
    color: black;
    font-weight: bold;
    font-size: 18px;
    font-family: times new roman;
}
QTableWidget {
    background-color: #e6f7ff;
}
""")

        self.tw1.setObjectName("tw1")
        self.tw1.setColumnCount(6)
        self.tw1.setRowCount(0)

        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            self.tw1.setHorizontalHeaderItem(i, item)

        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(250, 880, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")

        self.horizontalLayout.addWidget(self.frame)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form7)
        QtCore.QMetaObject.connectSlotsByName(form7)

        # my code
        self.form7 = form7
        self.b1.clicked.connect(self.back)
        db = sqlite3.connect("bank.db")
        a = "select * from trans"
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
        self.tw1.setShowGrid(True)
        self.tw1.setSortingEnabled(True)
        self.tw1.verticalHeader().setDefaultSectionSize(40)
        self.tw1.horizontalHeader().setStretchLastSection(True)
        self.tw1.setColumnWidth(2, 200)  
        self.tw1.setColumnWidth(4, 150)  

    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_form2()
        self.ui.setupUi(self.form2)
        self.form7.close()
        self.form2.show()

    def retranslateUi(self, form7):
        _translate = QtCore.QCoreApplication.translate
        form7.setWindowTitle(_translate("form7", "TRANSACTION REPORT"))

        item = self.tw1.horizontalHeaderItem(0)
        item.setText(_translate("form7", "TRANS ID"))
        item = self.tw1.horizontalHeaderItem(1)
        item.setText(_translate("form7", "ACC NO"))
        item = self.tw1.horizontalHeaderItem(2)
        item.setText(_translate("form7", "NAME"))
        item = self.tw1.horizontalHeaderItem(3)
        item.setText(_translate("form7", "DATE"))
        item = self.tw1.horizontalHeaderItem(4)
        item.setText(_translate("form7", "TRANS MODE"))
        item = self.tw1.horizontalHeaderItem(5)
        item.setText(_translate("form7", "AMOUNT"))

        self.b1.setText(_translate("form7", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form7 = QtWidgets.QWidget()
    ui = Ui_form7()
    ui.setupUi(form7)
    form7.showMaximized()
    sys.exit(app.exec_())
