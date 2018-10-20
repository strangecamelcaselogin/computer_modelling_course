from pathlib import Path
from PIL import Image

from app.learn_core.dataset import Dataset
from app.learn_core.dataset_loaders.abstract_dataset_loader import AbstractDatasetLoader


class SimpleFSLoader(AbstractDatasetLoader):
    """
    Загружает изображения из файловой системы
    структура каталогов должны быть следующей:

    dataset_name
    ├── test
    │   ├── class1
    │   │   └── image.png
    │   └── class2
    │       └── image (copy).png
    └── train
        ├── class1
        │   ├── image (2rd copy).png
        └── class2
            └── image (3th copy).png

    """
    def __init__(self, data_path, image_dimensions=(14, 14, 1)):
        """
        :param data_path: путь до папки с датасетами
        :param image_dimensions: размерность изображений
        """
        self.data_path: Path = Path(data_path).absolute()

        assert isinstance(image_dimensions, tuple) and len(image_dimensions) == 3
        # todo assert w == h?
        self.image_dimensions = image_dimensions

    def load(self, path) -> Dataset:
        """
        :param path: путь до dataset_name
        """
        name = Path(path).relative_to(self.data_path).name  # todo try except

        train_path = path / 'train'
        test_path = path / 'test'

        if not all([train_path.exists(), test_path.exists(), train_path.is_dir(), test_path.is_dir()]):
            raise Exception('DatasetLoader error: incorrect format')  # fixme

        train_images, train_labels, train_classes = self._load_classes(train_path)
        test_images, test_labels, test_classes = self._load_classes(test_path)

        if train_classes != test_classes:
            raise Exception('DatasetLoader error: test and train classes are different')  # fixme

        return Dataset(name, train_images, train_labels, test_images, test_labels,
                       classes=train_classes,
                       image_dimensions=self.image_dimensions)

    def _load_classes(self, path):
        images_by_class = {}
        images, labels = [], []

        classes_path = []
        for p in path.iterdir():
            if p.is_dir():
                classes_path.append(p)

        for cls_path in sorted(classes_path):
            cls_name = cls_path.name
            images_by_class[cls_name] = []
            for file in cls_path.iterdir():
                # загрузим мзображение и сконвертируем его в grayscale
                img = Image.open(file).convert('LA')

                # приведем его к желаемым размерам
                w, h, _ = self.image_dimensions
                img = img.resize((w, h), Image.ANTIALIAS)

                # todo convert to numpy here?

                images_by_class[cls_name].append(img)

        classes = []
        for class_name, files in images_by_class.items():
            class_number = len(classes)
            classes.append(class_name)
            labels.extend([class_number] * len(files))
            images.extend(files)

        return images, labels, classes
