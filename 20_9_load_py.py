# -*- coding: utf-8 -*-
from PyQt5 import  QtWidgets
import sys, ui_form

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_form.Ui_MyForm()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(app.exec_())
