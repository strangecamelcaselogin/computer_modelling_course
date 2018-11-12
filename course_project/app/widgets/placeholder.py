from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy


class PlaceholderWidget(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel('Система моделирования распознавания образов')
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setAlignment(Qt.AlignCenter)

        grid = QGridLayout()
        grid.addWidget(label)
        self.setLayout(grid)

        self.show()

    def update(self):
        pass
