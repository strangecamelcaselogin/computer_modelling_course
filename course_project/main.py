import logging
import sys
from setup import logger
from PyQt5 import QtWidgets

from app.main_window import MainWindow
from db import db


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    logger.info('App start')

    app = QtWidgets.QApplication(sys.argv)

    main_window = None
    try:
        db.connect()
        db.create_tables([])  # fixme

        main_window = MainWindow(app)
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        logger.exception(e)
    finally:
        db.close()  # todo check
        if main_window:
            main_window.stop()
        logger.info('App close')
