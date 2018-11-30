# -*- coding: utf-8 -*-
from PyQt5 import  QtWidgets, uic

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("ui.ui") #возвращает кортеж из ссылки на класс формы и ссылки на базовый класс
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # загрузка ui
    window = MyWindow() 
    window.show()
    sys.exit(app.exec_())