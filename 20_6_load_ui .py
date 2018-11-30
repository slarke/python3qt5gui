# -*- coding: utf-8 -*-
from PyQt5 import  QtWidgets, uic

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("ui.ui", self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # загрузка ui
    window = MyWindow() 
    window.show()
    sys.exit(app.exec_())