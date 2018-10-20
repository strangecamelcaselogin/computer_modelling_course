# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.session_menu = QtWidgets.QMenu(self.menubar)
        self.session_menu.setObjectName("session_menu")
        self.data_menu = QtWidgets.QMenu(self.menubar)
        self.data_menu.setObjectName("data_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.create_action = QtWidgets.QAction(MainWindow)
        self.create_action.setObjectName("create_action")
        self.load_action = QtWidgets.QAction(MainWindow)
        self.load_action.setObjectName("load_action")
        self.save_action = QtWidgets.QAction(MainWindow)
        self.save_action.setObjectName("save_action")
        self.save_as_action = QtWidgets.QAction(MainWindow)
        self.save_as_action.setObjectName("save_as_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.register_datacollection_action = QtWidgets.QAction(MainWindow)
        self.register_datacollection_action.setObjectName("register_datacollection_action")
        self.delete_datacollection_action = QtWidgets.QAction(MainWindow)
        self.delete_datacollection_action.setObjectName("delete_datacollection_action")
        self.session_menu.addAction(self.create_action)
        self.session_menu.addAction(self.load_action)
        self.session_menu.addAction(self.save_action)
        self.session_menu.addAction(self.save_as_action)
        self.session_menu.addSeparator()
        self.session_menu.addAction(self.exit_action)
        self.data_menu.addAction(self.register_datacollection_action)
        self.data_menu.addAction(self.delete_datacollection_action)
        self.menubar.addAction(self.session_menu.menuAction())
        self.menubar.addAction(self.data_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование"))
        self.session_menu.setTitle(_translate("MainWindow", "Сессия"))
        self.data_menu.setTitle(_translate("MainWindow", "Данные"))
        self.create_action.setText(_translate("MainWindow", "Новая"))
        self.load_action.setText(_translate("MainWindow", "Открыть"))
        self.save_action.setText(_translate("MainWindow", "Сохранить"))
        self.save_as_action.setText(_translate("MainWindow", "Сохранить как"))
        self.exit_action.setText(_translate("MainWindow", "Выйти"))
        self.register_datacollection_action.setText(_translate("MainWindow", "Указать"))
        self.delete_datacollection_action.setText(_translate("MainWindow", "Удалить"))

