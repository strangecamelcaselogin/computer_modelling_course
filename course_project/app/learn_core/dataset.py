import pickle


class Dataset:
    current_version = '1.1'

    class Data:
        def __init__(self, data, labels):
            self.data = data
            self.labels = labels

    def __init__(self, name, train_images, train_labels, test_images, test_labels, classes, image_dimensions):
        """

        :param name:
        :param train_images:
        :param train_labels:
        :param test_images:
        :param test_labels:
        :param classes:
        :param image_dimensions:
        """
        assert len(train_images) == len(train_labels)
        assert len(test_images) == len(test_labels)

        classes_set = set(list(range(len(classes))))
        assert classes_set == set(train_labels)
        assert classes_set == set(test_labels)
        assert isinstance(image_dimensions, tuple) and len(image_dimensions) == 3

        self.name = name

        self.train_data = Dataset.Data(train_images, train_labels)
        self.test_data = Dataset.Data(test_images, test_labels)

        self.classes = classes
        self.image_dimensions = image_dimensions

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
            'image_dimensions': self.image_dimensions
        })

    @classmethod
    def from_binary(cls, binary: bytes) -> 'Dataset':
        """ Десериализация """

        data = pickle.loads(binary)

        version = data['version']
        if version != cls.current_version:
            raise Exception('')  # fixme

        name = data['name']
        train_data = data['train_data']['data']
        train_labels = data['train_data']['labels']
        test_data = data['test_data']['data']
        test_labels = data['test_data']['labels']
        classes = data['classes']
        image_dimensions = data['image_dimensions']

        return Dataset(name, train_data, train_labels, test_data, test_labels, classes, image_dimensions)
