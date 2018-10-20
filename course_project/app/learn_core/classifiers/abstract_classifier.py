class AbstractClassifier:
    def learn(self, train_data):
        raise NotImplementedError

    def predict(self, images):
        raise NotImplementedError

    def validate(self, test_data):
        raise NotImplementedError
