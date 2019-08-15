# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import *

class Ui_MainWindow(object):

    def openNewWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 416)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 30, 231, 271))
        self.treeView.setObjectName("treeView")
        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(350, 30, 241, 271))
        self.treeView_2.setObjectName("treeView_2")
        self.addtextfile1 = QtWidgets.QPushButton(self.centralwidget)
        self.addtextfile1.setGeometry(QtCore.QRect(10, 310, 61, 41))
        self.addtextfile1.setText("")
        self.addtextfile1.setObjectName("addtextfile1")

        self.addtextfile1.clicked.connect(self.openNewWindow)


        self.addfile1 = QtWidgets.QPushButton(self.centralwidget)
        self.addfile1.setGeometry(QtCore.QRect(90, 310, 71, 41))
        self.addfile1.setText("")
        self.addfile1.setObjectName("addfile1")

        self.addfile1.clicked.connect(self.openNewWindow)


        self.delete1 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1.setGeometry(QtCore.QRect(180, 310, 61, 41))
        self.delete1.setText("")
        self.delete1.setObjectName("delete1")
        self.addtextfile2 = QtWidgets.QPushButton(self.centralwidget)
        self.addtextfile2.setGeometry(QtCore.QRect(350, 310, 61, 41))
        self.addtextfile2.setText("")
        self.addtextfile2.setObjectName("addtextfile2")

        self.addtextfile2.clicked.connect(self.openNewWindow)


        self.addfile2 = QtWidgets.QPushButton(self.centralwidget)
        self.addfile2.setGeometry(QtCore.QRect(430, 310, 71, 41))
        self.addfile2.setText("")
        self.addfile2.setObjectName("addfile2")

        self.addfile2.clicked.connect(self.openNewWindow)
        self.delete2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete2.setGeometry(QtCore.QRect(520, 310, 71, 41))
        self.delete2.setText("")
        self.delete2.setObjectName("delete2")
        self.send1 = QtWidgets.QPushButton(self.centralwidget)
        self.send1.setGeometry(QtCore.QRect(250, 100, 89, 25))
        self.send1.setText("")
        self.send1.setObjectName("send1")
        self.send2 = QtWidgets.QPushButton(self.centralwidget)
        self.send2.setGeometry(QtCore.QRect(250, 190, 89, 25))
        self.send2.setText("")
        self.send2.setObjectName("send2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
