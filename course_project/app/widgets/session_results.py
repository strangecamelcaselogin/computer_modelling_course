from PyQt5.QtWidgets import QWidget
from app.ui.session_results import Ui_session_results


class SessionResultsWidget(QWidget, Ui_session_results):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
