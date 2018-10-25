import math

from app.core.abstract_classifier import AbstractClassifier
from app.core.dataset import Dataset
from plugins.classifiers.potentials_fields.base import sq_dist


class PotentialFieldsClassifier(AbstractClassifier):
    able_to_classify_by = 2

    def __init__(self, classes, sample_dimensions):
        """
        :param sample_dimensions: размерности модели
        """
        super().__init__(classes, sample_dimensions)
        self._potential = []  # "история" для вычисления степени над e
        self.dimensions = len(sample_dimensions)

    @staticmethod
    def f(x, xk, a=1):
        """ Потенциальная функция: K(x, xk) """
        return a * math.e ** (-a * sq_dist(x, xk))

    @staticmethod
    def r(k, class_number):
        """ r """
        if class_number == 0:
            return 0 if k > 0 else 1
        elif class_number == 1:
            return 0 if k < 0 else -1
        else:
            raise Exception('Unknown class number, must be 0 or 1')

    def K(self, x):
        """ Значение кумулятивной функции """
        result = 0
        for idx, (r, xk) in enumerate(self._potential):
            result += result + r * self.f(x, xk)

        return result

    def learn(self, train_data: Dataset.Data, limit=100):
        """ Процесс обучения """
        images = train_data.data
        labels = train_data.labels

        success = total = 0
        while total < limit:
            for xk_new, cls in zip(images, labels):
                total += 1
                r = self.r(self.K(xk_new), cls)
                if abs(r) == 1:
                    success = 0
                    # добавляем новую запись в полином над степенью e
                    self._potential.append((r, xk_new))
                else:
                    success += 1
                    # если r равна 0 на протяжении N раз, то обучение завершено
                    if success >= len(images):
                        print(f'Break by success count. Total iterations: {total}, pow of e is: {len(self._potential)}')
                        return total
        else:
            print(f'Stop by reaching limit {limit}')

        return total

    def predict(self, image, quiet=True):
        assert len(image) == self.dimensions, 'Dimensions of new image and model must be equal'

        res = self.K(image)
        if not quiet:
            print(f'K({image}): {res}')

        # номер класса, 0 или 1
        return res < 0

    def save(self):
        pass

    @classmethod
    def load(cls):
        pass
