from pathlib import Path

from app.core.dataset import Dataset
from app.core.plugin_base import PluginBase


class AbstractDatasetLoader(PluginBase, abstract=True):
    plugins = []

    def __init__(self, data_path, sample_dimensions=(None, None, None)):
        """
        :param data_path: путь до папки с датасетами
        :param sample_dimensions: размерность данных
        """
        self.data_path: Path = Path(data_path).absolute()
        self.sample_dimensions = sample_dimensions

    @staticmethod
    def get_dialog(parent, data_path: str):
        raise NotImplementedError

    def load(self, path: Path) -> Dataset:
        raise NotImplementedError
