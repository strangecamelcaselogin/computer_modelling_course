# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'session_results.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_session_results(object):
    def setupUi(self, session_results):
        session_results.setObjectName("session_results")
        session_results.resize(828, 621)
        session_results.setWindowTitle("")
        self.gridLayout_2 = QtWidgets.QGridLayout(session_results)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(session_results)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(session_results)
        QtCore.QMetaObject.connectSlotsByName(session_results)

    def retranslateUi(self, session_results):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("session_results", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("session_results", "Точность"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("session_results", "Ошибки 1-го рода"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("session_results", "Ошибки 2-го рода"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("session_results", "Время обучения"))

