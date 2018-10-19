from pathlib import Path

from PyQt5.QtWidgets import QDialog, QFileDialog

from app.helpers import noty, get_relative_paths
from app.ui.create_dataset_widget import Ui_create_dataset_widget
from config import config


class CreateDatasetDialog(QDialog, Ui_create_dataset_widget):
    def __init__(self, model):
        super().__init__()

        self.model = model

        self.data_path = str(Path(config.data_path).absolute())

        self.learn_data = None
        self.test_data = None
        self.options = {}

        self.setupUi(self)
        self.connectUi()

    @property
    def name(self):
        return self.name_edit.text()

    def connectUi(self):
        self.learn_data_button.clicked.connect(self.load_learn_data)
        self.test_data_button.clicked.connect(self.load_test_data)
        self.create_dataset_button.clicked.connect(self.create_dataset)

    def pop_img_dialog(self, title):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, title, self.data_path, "Images (*.png)", options=options)
        return files

    def load_learn_data(self):
        files = self.pop_img_dialog("Загрузка Данных Для Обучения")
        self.learn_data = get_relative_paths(files, data_path=self.data_path)

    def load_test_data(self):
        files = self.pop_img_dialog("Загрузка Данных Для Валидации")
        self.test_data = get_relative_paths(files, data_path=self.data_path)

    def create_dataset(self):
        if not self.name or self.learn_data is None or self.test_data is None:
            noty("Ошибка", "Выберите данные")  # todo точнее пожалуйста
            return

        self.close()

    def exec_(self):
        super().exec_()

        ok = bool(self.learn_data and self.test_data and self.name)

        return ok, (self.name, self.learn_data, self.test_data, self.options)
