#my code
import sys
import add
import edit
import trans
import crep
import transmenu
#--------------

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form2(object):
    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(971, 805)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form2)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(210, 120, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(210, 210, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.frame)
        self.b3.setGeometry(QtCore.QRect(210, 300, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.frame)
        self.b4.setGeometry(QtCore.QRect(210, 390, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QPushButton(self.frame)
        self.b5.setGeometry(QtCore.QRect(210, 480, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QPushButton(self.frame)
        self.b6.setGeometry(QtCore.QRect(210, 570, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form2)
        QtCore.QMetaObject.connectSlotsByName(form2)
        #my code
        self.form2=form2
        self.b1.clicked.connect(self.add)
        self.b2.clicked.connect(self.edit)
        self.b3.clicked.connect(self.trans)
        self.b4.clicked.connect(self.crep)
        self.b5.clicked.connect(self.transmenu)
        self.b6.clicked.connect(self.exit)

    def add(self):
        self.form3 = QtWidgets.QWidget()
        self.ui = add.Ui_form3()
        self.ui.setupUi(self.form3)
        self.form2.close()
        self.form3.showMaximized()

    def edit(self):
        self.form4 = QtWidgets.QWidget()
        self.ui = edit.Ui_form4()
        self.ui.setupUi(self.form4)
        self.form2.close()
        self.form4.showMaximized()

    def trans(self):
        self.form5 = QtWidgets.QWidget()
        self.ui = trans.Ui_form5()
        self.ui.setupUi(self.form5)
        self.form2.close()
        self.form5.showMaximized()

    def crep(self):
        self.form6 = QtWidgets.QWidget()
        self.ui = crep.Ui_form6()
        self.ui.setupUi(self.form6)
        self.form2.close()
        self.form6.showMaximized()

    def transmenu(self):
        self.form8 = QtWidgets.QWidget()
        self.ui = transmenu.Ui_form8()
        self.ui.setupUi(self.form8)
        self.form2.close()
        self.form8.showMaximized()

    def exit(self):
        sys.exit()

    def retranslateUi(self, form2):
        _translate = QtCore.QCoreApplication.translate
        form2.setWindowTitle(_translate("form2", "MENU"))
        self.b1.setText(_translate("form2", "ADD CUSTOMER"))
        self.b2.setText(_translate("form2", "EDIT CUSTOMER"))
        self.b3.setText(_translate("form2", "ADD TRANSACTION"))
        self.b4.setText(_translate("form2", "CUSTOMER REPORT"))
        self.b5.setText(_translate("form2", "TRANSACTION REPORT"))
        self.b6.setText(_translate("form2", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form2 = QtWidgets.QWidget()
    ui = Ui_form2()
    ui.setupUi(form2)
    form2.showMaximized()
    sys.exit(app.exec_())
