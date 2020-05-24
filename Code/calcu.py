# Made by HoaxSnowden


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 529)
        MainWindow.setMinimumSize(QtCore.QSize(351, 529))
        MainWindow.setMaximumSize(QtCore.QSize(351, 529))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QFrame{\n"
"    background: rgba(0,0,0,120);\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel#numlabel{\n"
"    background: none;\n"
"}\n"
"\n"
"QLabel#numsolution{\n"
"    color: rgba(255,255,255,140);\n"
"	 font-size: 20px;\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-family: \"Cooper Black\";\n"
"    font-size: 28px;\n"
"    color: white;\n"
"    background-color: rgba(0,0,0, 180);\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(12,100,253,140);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(0,0,253,140);\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"}    \n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainscr = QtWidgets.QFrame(self.centralwidget)
        self.mainscr.setGeometry(QtCore.QRect(20, 20, 311, 171))
        self.mainscr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainscr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainscr.setObjectName("mainscr")
        self.numlabel = QtWidgets.QLabel(self.mainscr)
        self.numlabel.setGeometry(QtCore.QRect(10, 120, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.numlabel.setFont(font)
        self.numlabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.numlabel.setObjectName("numlabel")
        self.numsolution = QtWidgets.QLabel(self.mainscr)
        self.numsolution.setGeometry(QtCore.QRect(10, 80, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(24)
        self.numsolution.setFont(font)
        self.numsolution.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.numsolution.setObjectName("numsolution")
        self.numgrid = QtWidgets.QFrame(self.centralwidget)
        self.numgrid.setGeometry(QtCore.QRect(20, 200, 311, 311))
        self.numgrid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.numgrid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.numgrid.setObjectName("numgrid")
        self.C = QtWidgets.QPushButton(self.numgrid)
        self.C.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.C.setObjectName("C")
        self.CE = QtWidgets.QPushButton(self.numgrid)
        self.CE.setGeometry(QtCore.QRect(90, 10, 51, 51))
        self.CE.setObjectName("CE")
        self.modulo = QtWidgets.QPushButton(self.numgrid)
        self.modulo.setGeometry(QtCore.QRect(170, 10, 51, 51))
        self.modulo.setObjectName("modulo")
        self.divide = QtWidgets.QPushButton(self.numgrid)
        self.divide.setGeometry(QtCore.QRect(250, 10, 51, 51))
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.numgrid)
        self.multiply.setGeometry(QtCore.QRect(250, 70, 51, 51))
        self.multiply.setObjectName("multiply")
        self.subtract = QtWidgets.QPushButton(self.numgrid)
        self.subtract.setGeometry(QtCore.QRect(250, 130, 51, 51))
        self.subtract.setObjectName("subtract")
        self.add = QtWidgets.QPushButton(self.numgrid)
        self.add.setGeometry(QtCore.QRect(250, 190, 51, 51))
        self.add.setObjectName("add")
        self.equal = QtWidgets.QPushButton(self.numgrid)
        self.equal.setGeometry(QtCore.QRect(250, 250, 51, 51))
        self.equal.setObjectName("equal")
        self.seven = QtWidgets.QPushButton(self.numgrid)
        self.seven.setGeometry(QtCore.QRect(10, 70, 51, 51))
        self.seven.setObjectName("seven")
        self.nine = QtWidgets.QPushButton(self.numgrid)
        self.nine.setGeometry(QtCore.QRect(170, 70, 51, 51))
        self.nine.setObjectName("nine")
        self.eight = QtWidgets.QPushButton(self.numgrid)
        self.eight.setGeometry(QtCore.QRect(90, 70, 51, 51))
        self.eight.setObjectName("eight")
        self.six = QtWidgets.QPushButton(self.numgrid)
        self.six.setGeometry(QtCore.QRect(170, 130, 51, 51))
        self.six.setObjectName("six")
        self.three = QtWidgets.QPushButton(self.numgrid)
        self.three.setGeometry(QtCore.QRect(170, 190, 51, 51))
        self.three.setObjectName("three")
        self.dot = QtWidgets.QPushButton(self.numgrid)
        self.dot.setGeometry(QtCore.QRect(170, 250, 51, 51))
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.numgrid)
        self.zero.setGeometry(QtCore.QRect(10, 250, 131, 51))
        self.zero.setObjectName("zero")
        self.one = QtWidgets.QPushButton(self.numgrid)
        self.one.setGeometry(QtCore.QRect(10, 190, 51, 51))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.numgrid)
        self.two.setGeometry(QtCore.QRect(90, 190, 51, 51))
        self.two.setObjectName("two")
        self.five = QtWidgets.QPushButton(self.numgrid)
        self.five.setGeometry(QtCore.QRect(90, 130, 51, 51))
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.numgrid)
        self.four.setGeometry(QtCore.QRect(10, 130, 51, 51))
        self.four.setObjectName("four")
        self.six.raise_()
        self.subtract.raise_()
        self.zero.raise_()
        self.nine.raise_()
        self.four.raise_()
        self.three.raise_()
        self.add.raise_()
        self.CE.raise_()
        self.divide.raise_()
        self.multiply.raise_()
        self.seven.raise_()
        self.two.raise_()
        self.C.raise_()
        self.dot.raise_()
        self.modulo.raise_()
        self.one.raise_()
        self.eight.raise_()
        self.five.raise_()
        self.equal.raise_()
        self.bgimage = QtWidgets.QLabel(self.centralwidget)
        self.bgimage.setGeometry(QtCore.QRect(-140, 0, 981, 561))
        self.bgimage.setText("")
        self.bgimage.setPixmap(QtGui.QPixmap("images/6.jpg"))
        self.bgimage.setScaledContents(False)
        self.bgimage.setObjectName("bgimage")
        self.bgimage.raise_()
        self.mainscr.raise_()
        self.numgrid.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.C.clicked.connect(self.clrscr)
        self.CE.clicked.connect(self.clrscr)
        self.modulo.clicked.connect(self.clrscr)

        self.one.clicked.connect(lambda :self.pressnum("1"))
        self.two.clicked.connect(lambda :self.pressnum("2"))
        self.three.clicked.connect(lambda :self.pressnum("3"))
        self.four.clicked.connect(lambda :self.pressnum("4"))
        self.five.clicked.connect(lambda :self.pressnum("5"))
        self.six.clicked.connect(lambda :self.pressnum("6"))
        self.seven.clicked.connect(lambda :self.pressnum("7"))
        self.eight.clicked.connect(lambda :self.pressnum("8"))
        self.nine.clicked.connect(lambda :self.pressnum("9"))
        self.zero.clicked.connect(lambda :self.pressnum("0"))
        self.dot.clicked.connect(lambda :self.pressnum("."))
        self.add.clicked.connect(lambda :self.pressnum("+"))
        self.subtract.clicked.connect(lambda :self.pressnum("-"))
        self.multiply.clicked.connect(lambda :self.pressnum("*"))
        self.divide.clicked.connect(lambda :self.pressnum("/"))
        self.equal.clicked.connect(self.operate)

    def pressnum(self, num):
        cur = self.numlabel.text()
        cur += num
        self.numlabel.setText(cur)
        
    def clrscr(self):
    	self.numlabel.setText("")
    	self.numsolution.setText("")

    def operate(self):
    	current = self.numlabel.text()
    	self.numsolution.setText(current)

    	try:
    		ans = eval(current)
    	except:
    		self.showDialog()
    	else:
    		self.numlabel.setText(str(ans))
    	
    def showDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mathematical Error")
        msg.setText("The Mathematical Expression you entered is not valid")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.numlabel.setText(_translate("MainWindow", ""))
        self.numsolution.setText(_translate("MainWindow", ""))
        self.C.setText(_translate("MainWindow", "C"))
        self.CE.setText(_translate("MainWindow", "CE"))
        self.modulo.setText(_translate("MainWindow", "X"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.subtract.setText(_translate("MainWindow", "-"))
        self.add.setText(_translate("MainWindow", "+"))
        self.equal.setText(_translate("MainWindow", "="))
        self.seven.setText(_translate("MainWindow", "7"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.six.setText(_translate("MainWindow", "6"))
        self.three.setText(_translate("MainWindow", "3"))
        self.dot.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
