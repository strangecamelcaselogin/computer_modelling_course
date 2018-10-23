class AbstractClassifier:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.plugins.append(cls)

    def learn(self, train_data):
        raise NotImplementedError

    def predict(self, images):
        raise NotImplementedError

    def validate(self, test_data):
        raise NotImplementedError
