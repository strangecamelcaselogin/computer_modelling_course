from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit
from peewee import IntegrityError

from app.helpers import noty
from app.setup import logger
from app.model import Model
from app.ui.main_window import Ui_MainWindow
from app.widgets.placeholder import PlaceholderWidget

from app.widgets.session_selection import SessionSelectionDialog
from app.widgets.session_widget import SessionWidget


def text_dialog(self, header, message):
    text, ok = QInputDialog.getText(self, header, message, QLineEdit.Normal, "")
    if ok:
        return text


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application

        self.model = Model(self)

        self.session_widget = SessionWidget(self.model)
        self.placeholder_widget = PlaceholderWidget()

        self.setupUi(self)
        self.connectUi()

        self.current_widget = None
        self.show_placeholder()

        self.show()

    def connectUi(self):
        """ Соединяет слоты и сигналы """
        self.create_action.triggered.connect(self.new_session_dialog)
        self.load_action.triggered.connect(self.load_session_dialog)
        self.exit_action.triggered.connect(self.application.quit)

        self.session_widget.create_scenario_button.clicked.connect(self.new_scenario)
        # todo self.session_widget.run_button
        # todo self.session_widget.stop_button
        # todo self.session_widget.results_button

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
        selected_session_id = SessionSelectionDialog(self.model).exec_()

        if selected_session_id:
            session = self.model.get_session_by_id(selected_session_id)
            self.show_session()
            self.model.set_current_session(session)

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
        self.set_widget(self.session_widget)

    def new_scenario(self):
        name = text_dialog(self, "Создание нового сценария", "Введите имя сценария")

        if name:
            self.model.new_scenario(name)

    def update(self):
        """ Синхронизация с моделью, коллбек """
        if self.current_widget is not None:
            self.current_widget.update()

    def stop(self):
        """ Завершение работы """
        pass
