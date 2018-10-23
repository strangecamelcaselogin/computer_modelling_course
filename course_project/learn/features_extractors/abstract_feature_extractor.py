class AbstractFeatureExtractor:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.plugins.append(cls)

    def extract_features(self, img):
        raise NotImplementedError
