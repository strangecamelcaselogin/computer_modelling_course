from PyQt5.QtWidgets import QWidget
from app.ui.session_widget import Ui_SessionWidget


class SessionWidget(QWidget, Ui_SessionWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
