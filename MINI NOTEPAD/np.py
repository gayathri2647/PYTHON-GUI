from PyQt5.QtWidgets import*


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form1(object):
    def setupUi(self, form1):
        form1.setObjectName("form1")
        form1.resize(986, 875)
        self.b1 = QtWidgets.QPushButton(form1)
        self.b1.setGeometry(QtCore.QRect(160, 790, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(form1)
        self.b2.setGeometry(QtCore.QRect(380, 790, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(form1)
        self.b3.setGeometry(QtCore.QRect(600, 790, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.textEdit = QtWidgets.QTextEdit(form1)
        self.textEdit.setGeometry(QtCore.QRect(13, 16, 961, 761))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(25)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(form1)
        QtCore.QMetaObject.connectSlotsByName(form1)
        #my code
        self.form1=form1
        self.b1.clicked.connect(self.fn1)
        self.b2.clicked.connect(self.fn2)
        self.b3.clicked.connect(self.fn3)


    def fn1(self):
        f=QFileDialog.getOpenFileName(self.form1,"Open file", "d:\\", "*.txt")
        if f[0]:
            a=open(f[0],"r")
            b=a.read()
            self.te1.setPlainText(b)
            a.close()
    

    def fn2(self):
        f=QFileDialog.getSaveFileName(self.form1,"Save file", "d:\\", "*.txt")
        if f[0]:
            a=open(f[0],"w")
            b=self.te1.toPlainText()
            a.write(b)
            a.close()

    def fn3(self):
        self.te1.clear()

    def retranslateUi(self, form1):
        _translate = QtCore.QCoreApplication.translate
        form1.setWindowTitle(_translate("form1", "Mini Notepad "))
        self.b1.setText(_translate("form1", "OPEN"))
        self.b2.setText(_translate("form1", "SAVE"))
        self.b3.setText(_translate("form1", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QWidget()
    ui = Ui_form1()
    ui.setupUi(form1)
    form1.show()
    sys.exit(app.exec_())
