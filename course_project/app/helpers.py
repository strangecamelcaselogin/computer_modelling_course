from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon


def noty(title, message, icon_path='resources/icon.png'):
    """ Показ системной нотификации """
    # todo check if icon_path exists
    systemtray_icon = QSystemTrayIcon(QIcon(icon_path))
    systemtray_icon.show()
    systemtray_icon.showMessage(title, message)


def load_files(files_path):
    """ Возвращает список объектов, загруженных по соответствующим путям files_path """
    raise NotImplementedError()


def get_relative_paths(files_path, data_path):
    """ Возвращает относительные пути на файлы находящиеся в data_path """
    result = []

    # todo check if every file in data_path

    data_path = Path(data_path).absolute()
    for file in files_path:
        result.append(str(Path(file).relative_to(data_path)))

    return result
