from pathlib import Path
from typing import Type

from PyQt5.QtWidgets import QMainWindow, QAction
from peewee import IntegrityError

from app.core.abstract_dataset_loader import AbstractDatasetLoader
from app.helpers import noty, text_dialog
from app.setup import logger
from app.model import Model
from app.ui.main_window import Ui_MainWindow
from app.widgets.placeholder import PlaceholderWidget

from app.widgets.session_selection_dialog import SessionSelectionDialog
from app.widgets.session_widget import SessionWidget
from config import config


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application

        self.model = Model(self)

        self.data_path = Path(config.data_path).absolute()

        self.placeholder_widget = PlaceholderWidget()

        self.setupUi(self)
        self.connectUi()

        self.current_widget = None
        self.show_placeholder()

        self.show()

    def connectUi(self):
        """ Соединяет слоты и сигналы """
        # главное меню
        self.create_action.triggered.connect(self.new_session_dialog)
        self.load_action.triggered.connect(self.load_session_dialog)
        self.save_action.triggered.connect(self.not_implemented)  # todo
        self.save_as_action.triggered.connect(self.not_implemented)  # todo
        self.exit_action.triggered.connect(self.application.quit)

        # меню коллекций
        for loader_cls in self.model.get_dataset_loaders():
            action = QAction(loader_cls.__name__, self.create_data_collection_menu)
            action.triggered.connect(lambda useless_qt_param, c=loader_cls: self.new_dataset(c))  # fixme memory leak?
            self.create_data_collection_menu.addAction(action)

        self.delete_datacollection_action.triggered.connect(self.not_implemented)  # todo

        # todo меню инструментов

    def not_implemented(self):
        noty("not_implemented", "not_implemented")

    def set_widget(self, widget):
        """ Сменяет главный виджет """
        prev_widget = self.current_widget
        self.current_widget = widget

        if prev_widget is None:
            self.gridLayout.addWidget(self.current_widget)
        else:
            self.gridLayout.replaceWidget(prev_widget, self.current_widget)

    def show_placeholder(self):
        self.set_widget(self.placeholder_widget)

    def show_session(self):
        """ Открытие виджета сессии в главном окне """
        self.set_widget(SessionWidget(self.model))

    def new_session_dialog(self):
        """ создание новой сессии """
        success, session = False, None
        while True:
            name = text_dialog(self, "Создание новой сессии", "Имя новой сессии:")
            if name:
                try:
                    session = self.model.new_session(name)
                    success = True
                except IntegrityError:
                    noty('Ошибка', 'Сессия с таким именем уже существует')
                    continue
            break

        if success and session:
            self.show_session()
            self.model.set_current_session(session)

    def load_session_dialog(self):
        """ Открытие сессии из списка существующих """
        ok, selected_session_id = SessionSelectionDialog(self.model).exec_()

        if ok:
            session = self.model.get_session_by_id(selected_session_id)
            self.show_session()
            self.model.set_current_session(session)

    def new_dataset(self, loader_cls: Type[AbstractDatasetLoader]):
        path = loader_cls.get_dialog(self, str(self.data_path))
        if path:
            path = Path(path)
            name = path.relative_to(self.data_path).name
            try:
                self.model.new_data_collection(name, path, loader_cls)
            except Exception as e:
                logger.exception(e)
                noty("Ошибка", "Не получилось загрузить данные")  # fixme

    def update(self):
        """ Синхронизация с моделью, коллбек """
        if self.current_widget is not None:
            self.current_widget.update()

    def stop(self):
        """ Завершение работы """
        pass
