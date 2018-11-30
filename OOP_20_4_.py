# -*- coding: utf-8 -*-
from PyQt5 import  QtCore, QtWidgets
import OOP_20_3

class MyDialog(QtWidgets.QDialog): 
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent=None)
        self.myWidget = OOP_20_3.MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton("Change title")
        mainbox = QtWidgets.QVBoxLayout()
        mainbox.addWidget(self.myWidget)
        mainbox.addWidget(self.button)
        self.setLayout(mainbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("New label")
        self.button.setDisabled(True)

if __name__ == "__main__": 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog() #создаем экземпляр класса
    window.setWindowTitle("OOP style")
    window.resize(300, 70)
    window.show() #отбражаем окно
    sys.exit(app.exec_()) #запускаем цикл обработки событий