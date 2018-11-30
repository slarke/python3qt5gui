# -*- coding: utf-8 -*-
from PyQt5 import  QtWidgets, uic

Form, Base = uic.loadUiType("ui.ui")
class MyWindow(QtWidgets.QWidget, Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() 
    window.show()
    sys.exit(app.exec_())