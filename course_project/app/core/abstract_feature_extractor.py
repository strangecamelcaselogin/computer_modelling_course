from app.core.plugin_base import PluginBase


class AbstractFeatureExtractor(PluginBase, abstract=True):
    plugins = []

    def extract_features(self, img):
        raise NotImplementedError
