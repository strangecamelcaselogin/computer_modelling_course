from PyQt5.QtWidgets import QListWidgetItem, QDialog

from app.model import Model
from app.ui.session_selection import Ui_session_selection


class SessionSelectionItem(QListWidgetItem):
    def __init__(self, session):
        super().__init__(session.name)
        self.session_id = session.id


class SessionSelectionDialog(QDialog, Ui_session_selection):
    def __init__(self, model: Model):
        super().__init__()
        self.setModal(True)

        self.model = model
        self.selected_id = None

        self.setupUi(self)

        self.sessions_list.itemSelectionChanged.connect(self.select)
        self.sessions_list.itemDoubleClicked.connect(lambda item: self.select(item) and self.close())

        self.close_button.clicked.connect(self.close)
        self.load_button.clicked.connect(self.close)

    def exec_(self):
        sessions = self.model.get_sessions()
        for s in sessions:
            self.sessions_list.addItem(SessionSelectionItem(s))

        super().exec_()

        return self.selected_id

    def select(self, item: SessionSelectionItem=None):
        if item is None:
            item = self.sessions_list.currentItem()

        self.selected_id = item.session_id

        return True
