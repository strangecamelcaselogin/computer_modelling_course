from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from app.helpers import noty
from app.core.core import SessionProcessor
from app.model import Model
from app.ui.session_widget import Ui_SessionWidget
from app.widgets.scenario_dialog import ScenarioDialog


class SessionWidget(QWidget, Ui_SessionWidget):
    # todo block cell editing

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
        sd = ScenarioDialog(self.model)

        ok, scenario_data = sd.exec_()

        if ok:
            self.model.new_scenario(
                scenario_data['name'],
                scenario_data['data_collection'],
                scenario_data['feature_extractors'],
                scenario_data['classifier_class']
            )

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
            table.setItem(row_pos, 1, QTableWidgetItem(scenario.collection.name))
            table.setItem(row_pos, 2, QTableWidgetItem(scenario.feature_extractors))
            table.setItem(row_pos, 3, QTableWidgetItem(scenario.classifier))
            table.setItem(row_pos, 4, QTableWidgetItem(scenario.status.name))
