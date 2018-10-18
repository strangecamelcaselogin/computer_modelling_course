import logging
import sys
from app.setup import logger
from PyQt5 import QtWidgets

from app.widgets import MainWindow
from app.db import db
from app.models import Session, Scenario, DataCollection, Statistic


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    logger.info('App start')

    app = QtWidgets.QApplication(sys.argv)

    main_window = None
    try:
        db.connect()

        # todo arg ?
        # db.drop_tables([Session, Scenario, DataCollection, Statistic])
        db.create_tables([Session, Scenario, DataCollection, Statistic])

        main_window = MainWindow(app)
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        logger.exception(e)
    finally:
        db.close()
        if main_window:
            main_window.stop()
        logger.info('App close')
