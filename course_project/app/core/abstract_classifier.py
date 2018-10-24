from app.core.dataset import Dataset
from app.core.plugin_base import PluginBase


class AbstractClassifier(PluginBase, abstract=True):
    plugins = []

    able_to_classify_by = 0  # на сколько классов может классифицировать

    def learn(self, train_data: Dataset.Data):
        raise NotImplementedError

    def predict(self, image):
        raise NotImplementedError

    def validate(self, test_data: Dataset.Data):
        data, labels = test_data.data, test_data.labels

        errors = 0
        for sample, true_cls in zip(data, labels):
            cls = self.predict(sample)
            if cls != true_cls:
                errors += 1

        return errors, len(data)

    def save(self):
        raise NotImplementedError

    @classmethod
    def load(cls):
        raise NotImplementedError
