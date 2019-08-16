# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtGui import QIcon

from Tree import *

form_class = uic.loadUiType("Window.ui")[0]
form_class2 = uic.loadUiType("Window2.ui")[0]

t = Tree()

class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("Window2.ui",self)
        self.value = ""
        self.addButton.clicked.connect(self._add)
        self.cancelButton.clicked.connect(self.cancel)
        self.center()

    def cancel(self):
        self.close()

    def _add(self):
        self.value = self.lineEdit.text()
        print(self.value)
        self.close()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

    def closeEvent(self,event):
        event.accept()    

class MainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.children = ChildWindow()
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('67170.svg'))
        self.addCarpet1.clicked.connect(self.addCarpet_clicked)
        self.addFile1.clicked.connect(lambda:self.children.show())
        self.center()
        

    def center(self):

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()

        self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)

    def Agregar(self):
        QMessageBox.about(self,"Aviso","Carpeta Agregada!")

    def addCarpet_clicked(self):
        pass

    def addFile_clicked(self):
        t.add(self.children.value)
        
        

app = QtWidgets.QApplication(sys.argv)
MyWindow = MainWindow()
MyWindow.show()
app.exec_()       
