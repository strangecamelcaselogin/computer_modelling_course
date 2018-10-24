# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scenario_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scenario_dialog(object):
    def setupUi(self, scenario_dialog):
        scenario_dialog.setObjectName("scenario_dialog")
        scenario_dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(scenario_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(scenario_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(scenario_dialog)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_edit = QtWidgets.QLineEdit(scenario_dialog)
        self.name_edit.setObjectName("name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.data_collection_label = QtWidgets.QLabel(scenario_dialog)
        self.data_collection_label.setObjectName("data_collection_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.data_collection_label)
        self.data_collection_combo = QtWidgets.QComboBox(scenario_dialog)
        self.data_collection_combo.setObjectName("data_collection_combo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.data_collection_combo)
        self.feature_extraction_label = QtWidgets.QLabel(scenario_dialog)
        self.feature_extraction_label.setObjectName("feature_extraction_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.feature_extraction_label)
        self.feature_extraction_button = QtWidgets.QPushButton(scenario_dialog)
        self.feature_extraction_button.setObjectName("feature_extraction_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.feature_extraction_button)
        self.classifier_label = QtWidgets.QLabel(scenario_dialog)
        self.classifier_label.setObjectName("classifier_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.classifier_label)
        self.status_label = QtWidgets.QLabel(scenario_dialog)
        self.status_label.setObjectName("status_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.status_label)
        self.status_value_label = QtWidgets.QLabel(scenario_dialog)
        self.status_value_label.setText("")
        self.status_value_label.setObjectName("status_value_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.status_value_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.classifier_combo = QtWidgets.QComboBox(scenario_dialog)
        self.classifier_combo.setObjectName("classifier_combo")
        self.horizontalLayout.addWidget(self.classifier_combo)
        self.classifier_settings_button = QtWidgets.QToolButton(scenario_dialog)
        self.classifier_settings_button.setObjectName("classifier_settings_button")
        self.horizontalLayout.addWidget(self.classifier_settings_button)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(scenario_dialog)
        self.buttonBox.accepted.connect(scenario_dialog.accept)
        self.buttonBox.rejected.connect(scenario_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(scenario_dialog)

    def retranslateUi(self, scenario_dialog):
        _translate = QtCore.QCoreApplication.translate
        scenario_dialog.setWindowTitle(_translate("scenario_dialog", "Сценарий - "))
        self.name_label.setText(_translate("scenario_dialog", "Имя"))
        self.data_collection_label.setText(_translate("scenario_dialog", "Коллекция данных"))
        self.feature_extraction_label.setText(_translate("scenario_dialog", "Выделение признаков"))
        self.feature_extraction_button.setText(_translate("scenario_dialog", "Настроить"))
        self.classifier_label.setText(_translate("scenario_dialog", "Классификатор"))
        self.status_label.setText(_translate("scenario_dialog", "Статус"))
        self.classifier_settings_button.setText(_translate("scenario_dialog", "..."))

