from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from peewee import IntegrityError

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
        self.register_datacollection_action.triggered.connect(self.new_dataset)
        self.delete_datacollection_action.triggered.connect(self.not_implemented)  # todo

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

    def new_dataset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        path = QFileDialog.getExistingDirectory(self, 'Загрузить данные', str(self.data_path), options=options)
        if path:
            path = Path(path)
            name = path.relative_to(self.data_path).name
            try:
                self.model.new_data_collection(name, path)
            except Exception as e:
                noty("Ошибка", "Не получилось загрузить данные")  # fixme
                logger.exception(e)

    def update(self):
        """ Синхронизация с моделью, коллбек """
        if self.current_widget is not None:
            self.current_widget.update()

    def stop(self):
        """ Завершение работы """
        pass
