from app.core.abstract_classifier import AbstractClassifier


class NewClassifier(AbstractClassifier):
    def learn(self, train_data):
        pass

    def predict(self, images):
        pass

    def validate(self, test_data):
        pass
