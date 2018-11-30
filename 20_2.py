# -*- coding: utf-8 -*-
from PyQt5 import  QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('First prog Pyqt')
window.resize(300,70)
label = QtWidgets.QLabel('<center> Hello world </center>')
btnQuit = QtWidgets.QPushButton('&Close window')
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())