from typing import List

from app.learn_core.dataset import Dataset
from app.learn_core.features_extractors.abstract_feature_extractor import AbstractFeatureExtractor
from app.learn_core.classifiers.abstract_classifier import AbstractClassifier
from app.model import Model
from app.models import Session, Scenario, DataCollection


class SessionProcessor:
    def __init__(self, session: Session, model: Model):
        self.session = session
        self.model = model

        # todo thread

    def _process(self):
        scenarios = self.model.get_scenarios(self.session)

        for s in scenarios:
            dataset = self._load_dataset(s)
            fe = self._get_feature_extractors(s)

            processed_dataset = self._process_dataset(dataset, fe)

            classifier = self._instantiate_classifier(s)
            classifier.learn(processed_dataset.train_data)
            classifier.validate(processed_dataset.test_data)

            # todo save_classifier?

    def _load_dataset(self, current_scenario: Scenario) -> Dataset:
        dc: DataCollection = DataCollection.get(id=current_scenario.collection)
        return Dataset.from_binary(dc.data)

    def _get_feature_extractors(self, current_scenario: Scenario) -> List[AbstractFeatureExtractor]:
        raise NotImplementedError

    def _instantiate_classifier(self, current_scenario: Scenario) -> AbstractClassifier:
        raise NotImplementedError

    def _process_dataset(self, dataset: Dataset, feature_extractors: List[AbstractFeatureExtractor]) -> Dataset:
        raise NotImplementedError
