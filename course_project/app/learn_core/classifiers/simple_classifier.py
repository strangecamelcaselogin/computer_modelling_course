import time

from app.learn_core.classifiers.abstract_classifier import AbstractClassifier
from app.setup import logger


class SimpleClassifier(AbstractClassifier):
    def learn(self, train_data):
        logger.info('start learn')
        time.sleep(30)
        logger.info('stop learn')

    def predict(self, images):
        return 42

    def validate(self, test_data):
        pass
