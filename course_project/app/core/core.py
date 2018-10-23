from datetime import datetime
from threading import Thread
from typing import List

from learn.features_extractors import AbstractFeatureExtractor, SimpleExtractor
from learn.classifiers import AbstractClassifier, SimpleClassifier

from app.core.dataset import Dataset
from app.model import Model
from app.db_models import Scenario, DataCollection
from app.setup import logger


class SessionProcessor:
    def __init__(self, model: Model):
        self.model = model
        self._running = False
        self._thread = None

    def start(self):
        if self._running:
            raise Exception()  # fixme

        self._running = True
        self._thread = Thread(target=self._safe_wrapper)
        self._thread.start()

    def stop(self):
        if not self._running:
            raise Exception()  # fixme

        self._running = False
        if self._thread:
            self._thread.join()  # todo timeout

    def _safe_wrapper(self):
        try:
            self._process()
        except Exception as e:
            logger.exception(e)
            # todo send signal?

    def _process(self):
        scenarios = self.model.get_scenarios(self.model.current_session)

        while self._running:
            s = scenarios[0]  # todo pop new scenario

            dataset = self._load_dataset(s)
            fe = self._get_feature_extractors(s)

            processed_dataset = self._process_dataset(dataset, fe)

            classifier = self._instantiate_classifier(s)

            time = datetime.now()
            classifier.learn(processed_dataset)  # .train_data
            time = datetime.now() - time
            statistics = classifier.validate(processed_dataset)  # .test_data

            # todo save statistics, time
            # todo save_classifier?

    def _load_dataset(self, current_scenario: Scenario) -> Dataset:
        # todo current_scenario.collection
        first_collection = DataCollection.select()[0]

        # dc: DataCollection = DataCollection.get(id=current_scenario.collection)
        return Dataset.from_binary(first_collection .data)

    def _get_feature_extractors(self, current_scenario: Scenario) -> List[AbstractFeatureExtractor]:
        return [SimpleExtractor()]  # todo

    def _instantiate_classifier(self, current_scenario: Scenario) -> AbstractClassifier:
        return SimpleClassifier()  # todo

    def _process_dataset(self, dataset: Dataset, feature_extractors: List[AbstractFeatureExtractor]) -> Dataset:
        for fe in feature_extractors:
            pass  # todo

        return None
