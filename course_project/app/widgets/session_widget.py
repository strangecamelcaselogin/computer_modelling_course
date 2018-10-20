from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from app.model import Model
from app.ui.session_widget import Ui_SessionWidget


class SessionWidget(QWidget, Ui_SessionWidget):
    # todo editing

    def __init__(self, model: Model):
        super().__init__()
        self.model = model
        self.setupUi(self)

    def update(self):
        scenarios = self.model.get_current_scenarios()

        table = self.scenarios_table
        table.setRowCount(0)
        for scenario in scenarios:
            row_pos = table.rowCount()
            table.insertRow(row_pos)
            table.setItem(row_pos, 0, QTableWidgetItem(scenario.name))
            table.setItem(row_pos, 1, QTableWidgetItem('no data name'))
            table.setItem(row_pos, 2, QTableWidgetItem('no features'))
            table.setItem(row_pos, 3, QTableWidgetItem('no classifier'))
            table.setItem(row_pos, 4, QTableWidgetItem(scenario.status.name))
