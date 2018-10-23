from typing import Dict

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFormLayout, QDialog, QLabel, QDialogButtonBox, QListView


class MultiselectDialog(QDialog):
    """ Форма множественного выбора из опций """
    def __init__(self,  title, message, items: Dict[str, bool], parent=None):
        super(MultiselectDialog, self).__init__(parent=parent)
        form = QFormLayout(self)
        form.addRow(QLabel(message))

        self.list_view = QListView(self)
        form.addRow(self.list_view)

        model = QStandardItemModel(self.list_view)
        self.setWindowTitle(title)
        for key, checked in items.items():
            # create an item with a caption
            item = QStandardItem(key)
            item.setCheckable(True)
            item.setCheckState(Qt.Checked if checked else Qt.Unchecked)
            model.appendRow(item)

        self.list_view.setModel(model)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        form.addRow(button_box)

    def itemsSelected(self):
        selected = []
        model = self.list_view.model()
        i = 0
        while model.item(i):
            if model.item(i).checkState():
                selected.append(model.item(i).text())
            i += 1
        return selected
