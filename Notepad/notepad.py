from PyQt5.QtWidgets import *
import sys


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form1(object):
    def setupUi(self, form1):
        form1.setObjectName("form1")
        form1.resize(1347, 830)
        self.centralwidget = QtWidgets.QWidget(form1)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.te1 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.te1.setFont(font)
        self.te1.setObjectName("te1")
        self.horizontalLayout.addWidget(self.te1)
        form1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuSize = QtWidgets.QMenu(self.menubar)
        self.menuSize.setObjectName("menuSize")
        form1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form1)
        self.statusbar.setObjectName("statusbar")
        form1.setStatusBar(self.statusbar)
        self.miNew = QtWidgets.QAction(form1)
        self.miNew.setObjectName("miNew")
        self.actionOpen = QtWidgets.QAction(form1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(form1)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(form1)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(form1)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(form1)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(form1)
        self.actionPaste.setObjectName("actionPaste")
        self.actionBlue = QtWidgets.QAction(form1)
        self.actionBlue.setObjectName("actionBlue")
        self.actionRed = QtWidgets.QAction(form1)
        self.actionRed.setObjectName("actionRed")
        self.actionBlack = QtWidgets.QAction(form1)
        self.actionBlack.setObjectName("actionBlack")
        self.actionBrown = QtWidgets.QAction(form1)
        self.actionBrown.setObjectName("actionBrown")
        self.actionYellow = QtWidgets.QAction(form1)
        self.actionYellow.setObjectName("actionYellow")
        self.actionOrange = QtWidgets.QAction(form1)
        self.actionOrange.setObjectName("actionOrange")
        self.actionViolet = QtWidgets.QAction(form1)
        self.actionViolet.setObjectName("actionViolet")
        self.actionUndo = QtWidgets.QAction(form1)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(form1)
        self.actionRedo.setObjectName("actionRedo")
        self.action1 = QtWidgets.QAction(form1)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(form1)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(form1)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(form1)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(form1)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(form1)
        self.action6.setObjectName("action6")
        self.action7 = QtWidgets.QAction(form1)
        self.action7.setObjectName("action7")
        self.action8 = QtWidgets.QAction(form1)
        self.action8.setObjectName("action8")
        self.action9 = QtWidgets.QAction(form1)
        self.action9.setObjectName("action9")
        self.action10 = QtWidgets.QAction(form1)
        self.action10.setObjectName("action10")
        self.action11 = QtWidgets.QAction(form1)
        self.action11.setObjectName("action11")
        self.action12 = QtWidgets.QAction(form1)
        self.action12.setObjectName("action12")
        self.action13 = QtWidgets.QAction(form1)
        self.action13.setObjectName("action13")
        self.action14 = QtWidgets.QAction(form1)
        self.action14.setObjectName("action14")
        self.action15 = QtWidgets.QAction(form1)
        self.action15.setObjectName("action15")
        self.action16 = QtWidgets.QAction(form1)
        self.action16.setObjectName("action16")
        self.action17 = QtWidgets.QAction(form1)
        self.action17.setObjectName("action17")
        self.action18 = QtWidgets.QAction(form1)
        self.action18.setObjectName("action18")
        self.action19 = QtWidgets.QAction(form1)
        self.action19.setObjectName("action19")
        self.action20 = QtWidgets.QAction(form1)
        self.action20.setObjectName("action20")
        self.menuFile.addAction(self.miNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuColor.addAction(self.actionBlue)
        self.menuColor.addAction(self.actionRed)
        self.menuColor.addAction(self.actionBlack)
        self.menuColor.addAction(self.actionBrown)
        self.menuColor.addAction(self.actionYellow)
        self.menuColor.addAction(self.actionOrange)
        self.menuColor.addAction(self.actionViolet)
        self.menuSize.addAction(self.action1)
        self.menuSize.addAction(self.action2)
        self.menuSize.addAction(self.action3)
        self.menuSize.addAction(self.action4)
        self.menuSize.addAction(self.action5)
        self.menuSize.addAction(self.action6)
        self.menuSize.addAction(self.action7)
        self.menuSize.addAction(self.action8)
        self.menuSize.addAction(self.action9)
        self.menuSize.addAction(self.action10)
        self.menuSize.addAction(self.action11)
        self.menuSize.addAction(self.action12)
        self.menuSize.addAction(self.action13)
        self.menuSize.addAction(self.action14)
        self.menuSize.addAction(self.action15)
        self.menuSize.addAction(self.action16)
        self.menuSize.addAction(self.action17)
        self.menuSize.addAction(self.action18)
        self.menuSize.addAction(self.action19)
        self.menuSize.addAction(self.action20)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuSize.menuAction())

        self.retranslateUi(form1)
        QtCore.QMetaObject.connectSlotsByName(form1)
        #my code
        self.form1=form1
        self.miNew.triggered.connect(self.newfn)
        self.actionOpen.triggered.connect(self.openfn)
        self.actionSave.triggered.connect(self.savefn)
        self.actionExit.triggered.connect(self.exitfn)
        self.actionCut.triggered.connect(self.cutfn)
        self.actionCopy.triggered.connect(self.copyfn)
        self.actionPaste.triggered.connect(self.pastefn)
        self.actionRedo.triggered.connect(self.redofn)
        self.actionUndo.triggered.connect(self.undofn)
        self.actionBlue.triggered.connect(self.fn1)
        self.actionRed.triggered.connect(self.fn2)
        self.actionBlack.triggered.connect(self.fn3)
        self.actionBrown.triggered.connect(self.fn4)
        self.actionYellow.triggered.connect(self.fn5)
        self.actionOrange.triggered.connect(self.fn6)
        self.actionViolet.triggered.connect(self.fn7)
        self.action1.triggered.connect(self.fn8)
        self.action2.triggered.connect(self.fn9)
        self.action3.triggered.connect(self.fn10)
        self.action4.triggered.connect(self.fn11)
        self.action5.triggered.connect(self.fn12)
        self.action6.triggered.connect(self.fn13)
        self.action7.triggered.connect(self.fn14)
        self.action8.triggered.connect(self.fn15)
        self.action9.triggered.connect(self.fn16)
        self.action10.triggered.connect(self.fn17)
        self.action11.triggered.connect(self.fn18)
        self.action12.triggered.connect(self.fn19)
        self.action13.triggered.connect(self.fn20)
        self.action14.triggered.connect(self.fn21)
        self.action15.triggered.connect(self.fn22)
        self.action16.triggered.connect(self.fn23)
        self.action17.triggered.connect(self.fn24)
        self.action18.triggered.connect(self.fn25)
        self.action19.triggered.connect(self.fn26)
        self.action20.triggered.connect(self.fn27)


    def newfn(self):
        self.te1.clear()

    def openfn(self):
        f = QFileDialog.getOpenFileName(self.form1, "Open text file", "d:\\", "Text Files ( *.txt )")
        if f[0]:
            a=open(f[0],"r")
            b=a.read()
            self.te1.setText(b)
            a.close()

    def savefn(self):
        f=QFileDialog.getSaveFileName(self.form1,"save file","c:\\","*.txt")
        if f[0]:
            a=open(f[0],"w")
            b=self.te1.toPlainText()
            a.write(b)
            a.close()
            QMessageBox.about(self.form1,"FILE SAVE","File Saved Successfully")

    def exitfn(self):
        sys.exit()

    def cutfn(self):
        self.te1.cut()

    def copyfn(self):
        self.te1.copy()

    def pastefn(self):
        self.te1.paste()

    def redofn(self):
        self.te1.redo()

    def undofn(self):
        self.te1.undo()

    def fn1(self):
        self.te1.setStyleSheet("color:BLUE;")

    def fn2(self):
        self.te1.setStyleSheet("color:RED;")

    def fn3(self):
        self.te1.setStyleSheet("color:BLACK;")

    def fn4(self):
        self.te1.setStyleSheet("color:BROWN;")

    def fn5(self):
        self.te1.setStyleSheet("color:YELLOW;")

    def fn6(self):
        self.te1.setStyleSheet("color:ORANGE;")

    def fn7(self):
        self.te1.setStyleSheet("color:VIOLET;")

    def fn8(self):
        f=self.te1.font()
        f.setPointSize(1)
        self.te1.setFont(f)

    def fn9(self):
        f=self.te1.font()
        f.setPointSize(2)
        self.te1.setFont(f)

    def fn10(self):
        f=self.te1.font()
        f.setPointSize(3)
        self.te1.setFont(f)

    def fn11(self):
        f=self.te1.font()
        f.setPointSize(4)
        self.te1.setFont(f)

    def fn12(self):
        f=self.te1.font()
        f.setPointSize(5)
        self.te1.setFont(f)

    def fn13(self):
        f=self.te1.font()
        f.setPointSize(6)
        self.te1.setFont(f)

    def fn14(self):
        f=self.te1.font()
        f.setPointSize(7)
        self.te1.setFont(f)

    def fn15(self):
        f=self.te1.font()
        f.setPointSize(8)
        self.te1.setFont(f)

    def fn16(self):
        f=self.te1.font()
        f.setPointSize(9)
        self.te1.setFont(f)

    def fn17(self):
        f=self.te1.font()
        f.setPointSize(10)
        self.te1.setFont(f)

    def fn18(self):
        f=self.te1.font()
        f.setPointSize(11)
        self.te1.setFont(f)
        
    def fn19(self):
        f=self.te1.font()
        f.setPointSize(12)
        self.te1.setFont(f)

    def fn20(self):
        f=self.te1.font()
        f.setPointSize(13)
        self.te1.setFont(f)

    def fn21(self):
        f=self.te1.font()
        f.setPointSize(14)
        self.te1.setFont(f)

    def fn22(self):
        f=self.te1.font()
        f.setPointSize(15)
        self.te1.setFont(f)

    def fn23(self):
        f=self.te1.font()
        f.setPointSize(16)
        self.te1.setFont(f)

    def fn24(self):
        f=self.te1.font()
        f.setPointSize(17)
        self.te1.setFont(f)

    def fn25(self):
        f=self.te1.font()
        f.setPointSize(18)
        self.te1.setFont(f)
        
    def fn26(self):
        f=self.te1.font()
        f.setPointSize(19)
        self.te1.setFont(f)

    def fn27(self):
        f=self.te1.font()
        f.setPointSize(20)
        self.te1.setFont(f)

    def retranslateUi(self, form1):
        _translate = QtCore.QCoreApplication.translate
        form1.setWindowTitle(_translate("form1", "Notepad"))
        self.menuFile.setTitle(_translate("form1", "File"))
        self.menuEdit.setTitle(_translate("form1", "Edit"))
        self.menuColor.setTitle(_translate("form1", "Color"))
        self.menuSize.setTitle(_translate("form1", "Size"))
        self.miNew.setText(_translate("form1", "New"))
        self.miNew.setShortcut(_translate("form1", "Ctrl+N"))
        self.actionOpen.setText(_translate("form1", "Open"))
        self.actionOpen.setShortcut(_translate("form1", "Ctrl+O"))
        self.actionSave.setText(_translate("form1", "Save"))
        self.actionSave.setShortcut(_translate("form1", "Ctrl+S"))
        self.actionExit.setText(_translate("form1", "Exit"))
        self.actionExit.setShortcut(_translate("form1", "Ctrl+E"))
        self.actionCut.setText(_translate("form1", "Cut"))
        self.actionCut.setShortcut(_translate("form1", "Ctrl+X"))
        self.actionCopy.setText(_translate("form1", "Copy"))
        self.actionCopy.setShortcut(_translate("form1", "Ctrl+C"))
        self.actionPaste.setText(_translate("form1", "Paste"))
        self.actionPaste.setShortcut(_translate("form1", "Ctrl+V"))
        self.actionBlue.setText(_translate("form1", "Blue"))
        self.actionRed.setText(_translate("form1", "Red"))
        self.actionBlack.setText(_translate("form1", "Black"))
        self.actionBrown.setText(_translate("form1", "Brown"))
        self.actionYellow.setText(_translate("form1", "Yellow"))
        self.actionOrange.setText(_translate("form1", "Orange"))
        self.actionViolet.setText(_translate("form1", "Violet"))
        self.actionUndo.setText(_translate("form1", "Undo"))
        self.actionUndo.setShortcut(_translate("form1", "Ctrl+Z"))
        self.actionRedo.setText(_translate("form1", "Redo"))
        self.actionRedo.setShortcut(_translate("form1", "Ctrl+Y"))
        self.action1.setText(_translate("form1", "1"))
        self.action2.setText(_translate("form1", "2"))
        self.action3.setText(_translate("form1", "3"))
        self.action4.setText(_translate("form1", "4"))
        self.action5.setText(_translate("form1", "5"))
        self.action6.setText(_translate("form1", "6"))
        self.action7.setText(_translate("form1", "7"))
        self.action8.setText(_translate("form1", "8"))
        self.action9.setText(_translate("form1", "9"))
        self.action10.setText(_translate("form1", "10"))
        self.action11.setText(_translate("form1", "11"))
        self.action12.setText(_translate("form1", "12"))
        self.action13.setText(_translate("form1", "13"))
        self.action14.setText(_translate("form1", "14"))
        self.action15.setText(_translate("form1", "15"))
        self.action16.setText(_translate("form1", "16"))
        self.action17.setText(_translate("form1", "17"))
        self.action18.setText(_translate("form1", "18"))
        self.action19.setText(_translate("form1", "19"))
        self.action20.setText(_translate("form1", "20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form1 = QtWidgets.QMainWindow()
    ui = Ui_form1()
    ui.setupUi(form1)
    form1.show()
    sys.exit(app.exec_())
