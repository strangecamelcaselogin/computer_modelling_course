from PyQt5.QtWidgets import QMainWindow
from app.ui.main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, application):
        super().__init__()

        self.application = application

        self.ui = Ui_MainWindow()  # загружаем форму из .ui
        self.ui.setupUi(self)

    def stop(self):
        pass
