from collections import OrderedDict
from typing import Optional

from PyQt5.QtWidgets import QDialog

from app.helpers import noty
from app.model import Model
from app.db_models import Scenario
from app.ui.scenario_dialog import Ui_scenario_dialog
from app.widgets.multiselect_dialog import MultiselectDialog


class ScenarioDialog(QDialog, Ui_scenario_dialog):
    """ Диалог для создания и редактирования сценария """

    def __init__(self, model: Model, scenario: Optional[Scenario]=None, default_name='Новый сценарий'):
        super().__init__()
        self.setupUi(self)
        self.connectUi()

        self.model = model

        self.data_collections = model.get_data_collections()
        self.feature_extractors = model.get_feature_extractors()
        self.classifiers = model.get_classifiers()
        self.fill_lists()

        if scenario:
            self.name = scenario.name
            self.status = scenario.status  # todo for human
            self.selected_feature_extractors = scenario.feature_extractors
        else:
            self.name = default_name
            self.status = 'Создается'
            self.selected_feature_extractors = []

        self.setWindowTitle(self.name)

    def connectUi(self):
        self.feature_extraction_button.clicked.connect(self.show_feature_extraction_dialog)
        self.classifier_settings_button.clicked.connect(self.not_implemented)  # todo

    def not_implemented(self):
        noty("not_implemented", "not_implemented")

    def show_feature_extraction_dialog(self):
        items = OrderedDict()
        for fe in self.feature_extractors:
            fe_name = fe.__name__
            items[fe_name] = fe_name in self.selected_feature_extractors

        d = MultiselectDialog(
            "Настройка извлечения признаков",
            ("Выберите алгоритмы извлечения признаков.\n" 
             "Чтобы пропустить этап выделения признаков - не выбирайте ничего."),
            items)

        ok = d.exec_()
        if ok:
            self.selected_feature_extractors = d.itemsSelected()

    def fill_lists(self):
        for dc in self.data_collections:
            self.data_collection_combo.addItem(dc.name)

        for c in self.classifiers:
            self.classifier_combo.addItem(c.__name__)

    @property
    def name(self):
        return self.name_edit.text()

    @name.setter
    def name(self, value):
        self.name_edit.setText(value)

    @property
    def status(self):
        return self.status_value_label.text()

    @status.setter
    def status(self, value):
        self.status_value_label.setText(value)

    def exec_(self):
        status = super().exec_()

        if status:
            # todo as dataclass?
            return True, {
                'name': self.name,
                'data_collection': self.data_collections[self.data_collection_combo.currentIndex()],
                'feature_extractors': self.selected_feature_extractors if len(self.selected_feature_extractors) else None,
                'classifier_class': self.classifier_combo.currentText()
            }

        return False, {}
