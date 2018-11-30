# -*- coding: utf-8 -*-
from PyQt5 import  QtWidgets
import ui_form

class MyWindow(QtWidgets.QWidget, ui_form.Ui_MyForm):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
