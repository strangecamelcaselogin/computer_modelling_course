from typing import List

from app.core.plugin_base import PluginBase


class AbstractFeatureExtractor(PluginBase, abstract=True):
    plugins = []

    # количество признаков, которое выделяется из одного изображения
    features_amount = 0

    def extract_features(self, img) -> List[float]:
        """ Обрабатывает входное изображение img на N признаков """
        raise NotImplementedError
