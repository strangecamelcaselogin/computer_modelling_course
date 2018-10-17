# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'session_selection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_session_selection(object):
    def setupUi(self, session_selection):
        session_selection.setObjectName("session_selection")
        session_selection.resize(431, 600)
        session_selection.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(session_selection)
        self.gridLayout.setObjectName("gridLayout")
        self.sessions_list = QtWidgets.QListWidget(session_selection)
        self.sessions_list.setObjectName("sessions_list")
        self.gridLayout.addWidget(self.sessions_list, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_button = QtWidgets.QPushButton(session_selection)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout.addWidget(self.load_button)
        self.close_button = QtWidgets.QPushButton(session_selection)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(session_selection)
        QtCore.QMetaObject.connectSlotsByName(session_selection)

    def retranslateUi(self, session_selection):
        _translate = QtCore.QCoreApplication.translate
        self.load_button.setText(_translate("session_selection", "Выбрать"))
        self.close_button.setText(_translate("session_selection", "Отмена"))

