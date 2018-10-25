import time

from app.core.abstract_classifier import AbstractClassifier
from app.setup import logger


class DummyClassifier(AbstractClassifier):
    able_to_classify_by = 2

    def learn(self, train_data):
        logger.info('start learn')
        time.sleep(30)
        logger.info('stop learn')

    def predict(self, image):
        return 42

    def save(self):
        pass

    @classmethod
    def load(cls, data):
        pass
