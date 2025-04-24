#my code
import menu
import trep
import dtrep
import ctrep
#---------------
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form8(object):
    def setupUi(self, form8):
        form8.setObjectName("form8")
        form8.resize(1147, 826)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(form8)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(140, 240, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(140, 360, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.frame)
        self.b3.setGeometry(QtCore.QRect(140, 480, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.frame)
        self.b4.setGeometry(QtCore.QRect(140, 600, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(form8)
        QtCore.QMetaObject.connectSlotsByName(form8)
        #my code
        self.form8=form8
        self.b1.clicked.connect(self.ctrep)
        self.b2.clicked.connect(self.dtrep)
        self.b3.clicked.connect(self.trep)
        self.b4.clicked.connect(self.back)

    def ctrep(self):
        self.form9 = QtWidgets.QWidget()
        self.ui = ctrep.Ui_form9()
        self.ui.setupUi(self.form9)
        self.form8.close()
        self.form9.showMaximized()

    def dtrep(self):
        self.form10 = QtWidgets.QWidget()
        self.ui = dtrep.Ui_form10()
        self.ui.setupUi(self.form10)
        self.form8.close()
        self.form10.showMaximized()

    def trep(self):
        self.form7 = QtWidgets.QWidget()
        self.ui = trep.Ui_form7()
        self.ui.setupUi(self.form7)
        self.form8.close()
        self.form7.showMaximized()

    def back(self):
        self.form2 = QtWidgets.QWidget()
        self.ui = menu.Ui_Form()
        self.ui.setupUi(self.Form)
        self.form8.close()
        self.form2.showMaximized()


    def retranslateUi(self, form8):
        _translate = QtCore.QCoreApplication.translate
        form8.setWindowTitle(_translate("form8", "TRANSACTION MENU"))
        self.b1.setText(_translate("form8", "SEARCH CUSTOMER TRANSACTION"))
        self.b2.setText(_translate("form8", "SEARCH TRANSACTIONS BY DATE"))
        self.b3.setText(_translate("form8", "TRANSACTION HISTORY"))
        self.b4.setText(_translate("form8", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form8 = QtWidgets.QWidget()
    ui = Ui_form8()
    ui.setupUi(form8)
    form8.show()
    sys.exit(app.exec_())
