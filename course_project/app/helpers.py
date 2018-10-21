from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QInputDialog, QLineEdit


def noty(title, message, icon_path='resources/icon.png'):
    """ Показ системной нотификации """
    # todo check if icon_path exists
    systemtray_icon = QSystemTrayIcon(QIcon(icon_path))
    systemtray_icon.show()
    systemtray_icon.showMessage(title, message)


def text_dialog(self, header, message):
    text, ok = QInputDialog.getText(self, header, message, QLineEdit.Normal, "")
    if ok:
        return text