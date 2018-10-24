class AbstractDatasetLoader:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.plugins.append(cls)

    def load(self, path):
        raise NotImplementedError
