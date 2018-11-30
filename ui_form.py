# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(300, 70)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MyForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnQuit = QtWidgets.QPushButton(MyForm)
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout.addWidget(self.btnQuit)
        self.label = QtWidgets.QLabel(MyForm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(MyForm)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "Load from UI"))
        self.btnQuit.setText(_translate("MyForm", "Quit"))
        self.label.setText(_translate("MyForm", "Text!!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyForm = QtWidgets.QWidget()
    ui = Ui_MyForm()
    ui.setupUi(MyForm)
    MyForm.show()
    sys.exit(app.exec_())

