import pickle


class Dataset:
    current_version = '1.2'

    class Data:
        def __init__(self, data, labels):
            self.data = data
            self.labels = labels

    def __init__(self, name, train_data, train_labels, test_data, test_labels, classes, sample_dimensions):
        """
        Класс для хранения обучающих и валидационных данных
        :param name: Имя датасета
        :param train_data: тренировочные данные (картинки, вектора, все что угодно)
        :param train_labels: разметка классов данных (начиная от 0)
        :param test_data: тестовые данные
        :param test_labels: тестовая разметка
        :param classes: список имен классов
        :param sample_dimensions: размерность данных, tuple<w, h, z>
        """
        assert len(train_data) == len(train_labels)
        assert len(test_data) == len(test_labels)

        classes_numbers_set = set(list(range(len(classes))))
        assert classes_numbers_set == set(train_labels)
        assert classes_numbers_set == set(test_labels)
        assert isinstance(sample_dimensions, tuple)

        self.name = name

        self.train_data = Dataset.Data(train_data, train_labels)
        self.test_data = Dataset.Data(test_data, test_labels)

        self.classes = classes
        self.sample_dimensions = sample_dimensions

    @property
    def classes_count(self):
        return len(self.classes)

    def as_binary(self) -> bytes:
        """ Сериализация в бинарное представление """

        return pickle.dumps({
            'version': self.current_version,
            'name': self.name,
            'train_data': {
                'data': self.train_data.data,
                'labels': self.train_data.labels,
            },
            'test_data': {
               'data': self.test_data.data,
               'labels': self.test_data.labels,
            },
            'classes': self.classes,
            'sample_dimensions': self.sample_dimensions
        })

    @classmethod
    def from_binary(cls, binary: bytes) -> 'Dataset':
        """ Десериализация """

        data = pickle.loads(binary)

        version = data['version']
        if version != cls.current_version:
            raise Exception('Too old')  # fixme

        name = data['name']
        train_data = data['train_data']['data']
        train_labels = data['train_data']['labels']
        test_data = data['test_data']['data']
        test_labels = data['test_data']['labels']
        classes = data['classes']
        sample_dimensions = data['sample_dimensions']

        return Dataset(
            name,
            train_data, train_labels,
            test_data, test_labels,
            classes,
            sample_dimensions)
