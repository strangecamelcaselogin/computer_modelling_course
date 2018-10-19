from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon


def noty(title, message, icon_path='resources/icon.png'):
    # todo check if icon_path exists
    systemtray_icon = QSystemTrayIcon(QIcon(icon_path))
    systemtray_icon.show()
    systemtray_icon.showMessage(title, message)
