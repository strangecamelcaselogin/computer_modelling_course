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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.session = QtWidgets.QMenu(self.menubar)
        self.session.setObjectName("session")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.create = QtWidgets.QAction(MainWindow)
        self.create.setObjectName("create")
        self.load = QtWidgets.QAction(MainWindow)
        self.load.setObjectName("load")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.session.addAction(self.create)
        self.session.addAction(self.load)
        self.session.addAction(self.save)
        self.session.addAction(self.save_as)
        self.session.addSeparator()
        self.session.addAction(self.exit)
        self.menubar.addAction(self.session.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование"))
        self.session.setTitle(_translate("MainWindow", "Сессия"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.create.setText(_translate("MainWindow", "Новая"))
        self.load.setText(_translate("MainWindow", "Открыть"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.save_as.setText(_translate("MainWindow", "Сохранить как"))
        self.exit.setText(_translate("MainWindow", "Выйти"))

