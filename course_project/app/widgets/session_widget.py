from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from app.helpers import text_dialog, noty
from app.learn_core.core import SessionProcessor
from app.model import Model
from app.ui.session_widget import Ui_SessionWidget


class SessionWidget(QWidget, Ui_SessionWidget):
    # todo editing

    def __init__(self, model: Model):
        super().__init__()
        self.model = model

        self.session = model.current_session
        self.session_processor = SessionProcessor(self.model)

        self.setupUi(self)
        self.connectUi()

    def connectUi(self):
        self.create_scenario_button.clicked.connect(self.new_scenario)
        self.run_button.clicked.connect(self.run_session)
        self.stop_button.clicked.connect(self.stop_session)
        self.results_button.clicked.connect(self.not_implemented)  # todo

    def not_implemented(self):
        noty("not_implemented", "not_implemented")

    def new_scenario(self):
        name = text_dialog(self, "Создание нового сценария", "Введите имя сценария")

        if name:
            self.model.new_scenario(name)

    def run_session(self):
        noty('msg', 'run')
        self.session_processor.start()

    def stop_session(self):
        noty('msg', 'stop')
        self.session_processor.stop()

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
