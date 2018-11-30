# -*- coding: utf-8 -*-
from PyQt5 import  QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget): #определяем класс который наследует Qwidget
    def __init__(self, parent=None): #опрределяет конструктор класса.
        #В кач-ве пар-ров он принимает ссылки на экземпляр класса
        QtWidgets.QWidget.__init__(self, parent=None)
        self.label = QtWidgets.QLabel("Hello world!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Close window")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__":
    #Создание объекта приложения и экземпляра класса 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() #создаем экземпляр класса
    window.setWindowTitle("OOP style")
    window.resize(300, 70)
    window.show() #отбражаем окно
    sys.exit(app.exec_()) #запускаем цикл обработки событий