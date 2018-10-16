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
        self.gridLayout_2 = QtWidgets.QGridLayout(SessionWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create = QtWidgets.QPushButton(SessionWidget)
        self.create.setObjectName("create")
        self.horizontalLayout_2.addWidget(self.create)
        self.run = QtWidgets.QPushButton(SessionWidget)
        self.run.setObjectName("run")
        self.horizontalLayout_2.addWidget(self.run)
        self.stop = QtWidgets.QPushButton(SessionWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scenarios_widget = QtWidgets.QTableWidget(SessionWidget)
        self.scenarios_widget.setRowCount(0)
        self.scenarios_widget.setObjectName("scenarios_widget")
        self.scenarios_widget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.scenarios_widget.setHorizontalHeaderItem(4, item)
        self.scenarios_widget.horizontalHeader().setVisible(True)
        self.scenarios_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.scenarios_widget.horizontalHeader().setHighlightSections(True)
        self.scenarios_widget.horizontalHeader().setMinimumSectionSize(100)
        self.scenarios_widget.horizontalHeader().setSortIndicatorShown(False)
        self.scenarios_widget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.scenarios_widget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SessionWidget)
        QtCore.QMetaObject.connectSlotsByName(SessionWidget)

    def retranslateUi(self, SessionWidget):
        _translate = QtCore.QCoreApplication.translate
        self.create.setText(_translate("SessionWidget", "Новый сценарий"))
        self.run.setText(_translate("SessionWidget", "Запустить"))
        self.stop.setText(_translate("SessionWidget", "Остановить"))
        item = self.scenarios_widget.horizontalHeaderItem(0)
        item.setText(_translate("SessionWidget", "Имя"))
        item = self.scenarios_widget.horizontalHeaderItem(1)
        item.setText(_translate("SessionWidget", "Признаки"))
        item = self.scenarios_widget.horizontalHeaderItem(2)
        item.setText(_translate("SessionWidget", "Классификатор"))
        item = self.scenarios_widget.horizontalHeaderItem(3)
        item.setText(_translate("SessionWidget", "Статус"))
        item = self.scenarios_widget.horizontalHeaderItem(4)
        item.setText(_translate("SessionWidget", "Результат"))

