# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'session_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SessionWidget(object):
    def setupUi(self, SessionWidget):
        SessionWidget.setObjectName("SessionWidget")
        SessionWidget.resize(813, 730)
        SessionWidget.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(SessionWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_session_button = QtWidgets.QPushButton(SessionWidget)
        self.create_session_button.setObjectName("create_session_button")
        self.horizontalLayout_2.addWidget(self.create_session_button)
        self.run_button = QtWidgets.QPushButton(SessionWidget)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        self.stop_button = QtWidgets.QPushButton(SessionWidget)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_2.addWidget(self.stop_button)
        self.results_button = QtWidgets.QPushButton(SessionWidget)
        self.results_button.setObjectName("results_button")
        self.horizontalLayout_2.addWidget(self.results_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scenarios_table = QtWidgets.QTableWidget(SessionWidget)
        self.scenarios_table.setRowCount(0)
        self.scenarios_table.setObjectName("scenarios_table")
        self.scenarios_table.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_table.setHorizontalHeaderItem(5, item)
        self.scenarios_table.horizontalHeader().setVisible(True)
        self.scenarios_table.horizontalHeader().setCascadingSectionResizes(False)
        self.scenarios_table.horizontalHeader().setHighlightSections(True)
        self.scenarios_table.horizontalHeader().setMinimumSectionSize(100)
        self.scenarios_table.horizontalHeader().setSortIndicatorShown(False)
        self.scenarios_table.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.scenarios_table)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SessionWidget)
        QtCore.QMetaObject.connectSlotsByName(SessionWidget)

    def retranslateUi(self, SessionWidget):
        _translate = QtCore.QCoreApplication.translate
        self.create_session_button.setText(_translate("SessionWidget", "Новый сценарий"))
        self.run_button.setText(_translate("SessionWidget", "Запустить"))
        self.stop_button.setText(_translate("SessionWidget", "Остановить"))
        self.results_button.setText(_translate("SessionWidget", "Результаты"))
        item = self.scenarios_table.horizontalHeaderItem(0)
        item.setText(_translate("SessionWidget", "Имя"))
        item = self.scenarios_table.horizontalHeaderItem(1)
        item.setText(_translate("SessionWidget", "Данные 1"))
        item = self.scenarios_table.horizontalHeaderItem(2)
        item.setText(_translate("SessionWidget", "Данные 2"))
        item = self.scenarios_table.horizontalHeaderItem(3)
        item.setText(_translate("SessionWidget", "Признаки"))
        item = self.scenarios_table.horizontalHeaderItem(4)
        item.setText(_translate("SessionWidget", "Классификатор"))
        item = self.scenarios_table.horizontalHeaderItem(5)
        item.setText(_translate("SessionWidget", "Статус"))

