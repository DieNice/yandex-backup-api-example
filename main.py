# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

from PyQt5.QtWidgets import QLabel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


app = QtWidgets.QApplication([])
win = uic.loadUi("gui/main.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())