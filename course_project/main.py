import logging
import sys
import argparse
from PyQt5 import QtWidgets

from app.setup import logger
from app.widgets import MainWindow
from app.db import db
from app.db_models import Session, Scenario, DataCollection, Statistic

from learn.dataset_loaders import AbstractDatasetLoader
from learn.features_extractors import AbstractFeatureExtractor
from learn.classifiers import AbstractClassifier


def show_plugins():
    for plugabble in [AbstractDatasetLoader, AbstractFeatureExtractor, AbstractClassifier]:
        names = '\n\t'.join(map(str, plugabble.plugins))
        logger.info(f"{plugabble.__name__} plugins detected:\n\t{names}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Computer modelling course project...')
    parser.add_argument('--drop', action='store_true', default=False, help='Drop for database drop')
    args = parser.parse_args()

    logger.setLevel(logging.DEBUG)
    logger.info('App start')

    show_plugins()

    app = QtWidgets.QApplication(sys.argv)

    main_window = None
    try:
        db.connect()

        models = [Session, Scenario, DataCollection, Statistic]
        if args.drop:
            db.drop_tables(models)
            logger.info(f'Models {models} deleted.')

        db.create_tables(models)
        logger.info(f'Models {models} recreated.')

        main_window = MainWindow(app)
        sys.exit(app.exec())
    except Exception as e:
        logger.exception(e)
    finally:
        db.close()
        if main_window:
            main_window.stop()

        logger.info('App close')
