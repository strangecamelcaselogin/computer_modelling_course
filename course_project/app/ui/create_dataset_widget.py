# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dataset_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_create_dataset_widget(object):
    def setupUi(self, create_dataset_widget):
        create_dataset_widget.setObjectName("create_dataset_widget")
        create_dataset_widget.resize(455, 331)
        self.gridLayout = QtWidgets.QGridLayout(create_dataset_widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.bottom_message = QtWidgets.QLabel(create_dataset_widget)
        self.bottom_message.setText("")
        self.bottom_message.setObjectName("bottom_message")
        self.gridLayout.addWidget(self.bottom_message, 5, 0, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(create_dataset_widget)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.learn_data_button = QtWidgets.QPushButton(create_dataset_widget)
        self.learn_data_button.setObjectName("learn_data_button")
        self.horizontalLayout.addWidget(self.learn_data_button)
        self.test_data_button = QtWidgets.QPushButton(create_dataset_widget)
        self.test_data_button.setObjectName("test_data_button")
        self.horizontalLayout.addWidget(self.test_data_button)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.top_message = QtWidgets.QLabel(create_dataset_widget)
        self.top_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.top_message.setObjectName("top_message")
        self.gridLayout.addWidget(self.top_message, 2, 0, 1, 1)
        self.create_dataset_button = QtWidgets.QPushButton(create_dataset_widget)
        self.create_dataset_button.setObjectName("create_dataset_button")
        self.gridLayout.addWidget(self.create_dataset_button, 7, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(create_dataset_widget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.retranslateUi(create_dataset_widget)
        QtCore.QMetaObject.connectSlotsByName(create_dataset_widget)

    def retranslateUi(self, create_dataset_widget):
        _translate = QtCore.QCoreApplication.translate
        create_dataset_widget.setWindowTitle(_translate("create_dataset_widget", "Содание Коллекции Данных"))
        self.learn_data_button.setText(_translate("create_dataset_widget", "Данные для обучения"))
        self.test_data_button.setText(_translate("create_dataset_widget", "Данные для валидации"))
        self.top_message.setText(_translate("create_dataset_widget", "Выберите два набора данных:\n"
" - Для обучения классификатора \n"
" - Для валидации результатов"))
        self.create_dataset_button.setText(_translate("create_dataset_widget", "Создать"))
        self.name_label.setText(_translate("create_dataset_widget", "Введите имя новой коллекции:"))

