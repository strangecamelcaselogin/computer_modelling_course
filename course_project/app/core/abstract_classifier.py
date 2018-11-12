from typing import List, Tuple, Any

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

    def learn(self, train_data: Dataset.Data):
        """
        Обучение модели
        :param train_data: обучающая часть датасета
        """
        raise NotImplementedError

    def predict(self, image) -> int:
        """
        Классификация образа image
        :param image: образ
        :return: номер класса
        """
        raise NotImplementedError

    def validate(self, test_data: Dataset.Data) -> List[Tuple[int, int, Any]]:
        """
        Валидация качества обучения
        :param test_data: тестовая часть датасета
        """
        data, labels = test_data.data, test_data.labels

        errors = []
        for sample, true_cls in zip(data, labels):
            cls = self.predict(sample)
            if cls != true_cls:
                errors.append((cls, true_cls, sample))

        return errors

    def save(self) -> bytes:
        """ Метод сохранения модели в бинарном виде """
        raise NotImplementedError

    @classmethod
    def load(cls, data: bytes) -> 'AbstractClassifier':
        """ Восстановление экземпляра AbstractClassifier из сериализованного вида """
        raise NotImplementedError
