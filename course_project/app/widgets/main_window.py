from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit
from peewee import IntegrityError

from app.setup import logger
from app.controller import Controller
from app.model import Model
from app.ui.main_window import Ui_MainWindow

from app.widgets.session_selection import SessionSelectionDialog
from app.widgets.session_widget import SessionWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application

        self.model = Model()
        self.controller = Controller(self.model, self)

        self.session_widget = SessionWidget()
        self.current_widget = None

        self.setupUi(self)
        self.connectUi()

    def connectUi(self):
        """ Соединяет слоты и сигналы """
        self.create_action.triggered.connect(self.new_session_dialog)
        self.load_action.triggered.connect(self.load_session_dialog)

        # todo
        # todo

        self.exit_action.triggered.connect(self.application.quit)

    def new_session_dialog(self):
        """ создание новой сессии """
        success, session = False, None
        while True:
            name, ok = QInputDialog.getText(self, "Создание новой сессии",
                                            "Имя новой сессии:", QLineEdit.Normal, "")
            if ok:
                try:
                    session = self.controller.new_session(name)
                    success = True
                except IntegrityError as e:
                    logger.info(e)
                    continue
            break

        if success and session:
            self.load_session(session)

    def load_session_dialog(self):
        """ Открытие сессии из списка существующих """
        selected_session_id = SessionSelectionDialog(self.model).exec_()

        if selected_session_id:
            session = self.model.get_session_by_id(selected_session_id)
            self.load_session(session)

    def load_session(self, session):
        """ Открытие виджета сессии в главном окне """
        prev_widget = self.current_widget
        self.current_widget = self.session_widget
        # todo sessionWidget set data
        if prev_widget is None:
            self.gridLayout.addWidget(self.current_widget)
        else:
            # todo check
            self.gridLayout.replaceWidget(prev_widget, self.current_widget)

    def update(self):
        """ Синхронизация с моделью, коллбек """
        pass

    def stop(self):
        """ Завершение работы """
        pass
