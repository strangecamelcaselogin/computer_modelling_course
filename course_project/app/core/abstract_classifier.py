from typing import List, Tuple

from app.core.dataset import Dataset
from app.core.plugin_base import PluginBase
from app.core.protocol import Protocol


class AbstractClassifier(PluginBase, abstract=True):
    plugins = []

    able_to_classify_by = 0  # на сколько классов может классифицировать

    def __init__(self, classes: List[int], sample_dimensions: Tuple[int], protocol: Protocol):
        self.classes = classes
        self.sample_dimensions = sample_dimensions
        self.protocol = protocol

    def learn(self, train_data: Dataset.Data):  # todo
        raise NotImplementedError

    def predict(self, image):  # todo
        raise NotImplementedError

    def validate(self, test_data: Dataset.Data):  # todo typeing
        data, labels = test_data.data, test_data.labels

        errors = 0
        for sample, true_cls in zip(data, labels):
            cls = self.predict(sample)
            if cls != true_cls:
                errors += 1

        return errors, len(data)

    def save(self) -> bytes:
        raise NotImplementedError

    @classmethod
    def load(cls, data: bytes) -> 'AbstractClassifier':
        raise NotImplementedError
