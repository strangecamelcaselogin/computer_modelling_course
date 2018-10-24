import math

from app.core.abstract_classifier import AbstractClassifier
from app.core.dataset import Dataset
from plugins.classifiers.potentials_fields.base import sq_dist


class StochasticPotentialFieldsClassifier(AbstractClassifier):
    able_to_classify_by = 2

    def __init__(self, classes, sample_dimensions):
        """
        :param sample_dimensions: размерность модели
        """
        self.classes = classes
        self._potentials = {i: [] for i in classes}  # "история" для вычисления степени над e

        self.dimensions = len(sample_dimensions)

    @staticmethod
    def f(x, xk, a=1):
        """ Потенциальная функция: K(x, xk) """
        return a * math.e ** (-a * sq_dist(x, xk))

    def K(self, x, for_cls):
        """ Значение кумулятивной функции """

        assert for_cls in self._potentials, 'for_cls must be one of labels index'

        result = 0
        for idx, (j, xk) in enumerate(self._potentials[for_cls]):
            result += result + j * self.f(x, xk)

        return result

    def learn(self, train_data: Dataset.Data, limit=100):
        images = train_data.data
        labels = train_data.labels

        potentials_j = {i: 1 for i in self.classes}
        success = total = 0
        while total < limit:
            print('Global Iteration.')

            for xk_new, target_cls in zip(images, labels):
                total += 1
                print(f'Local iteration: {total}, target_cls: {target_cls}')
                for cls in self.classes:
                    res = self.K(xk_new, for_cls=cls)

                    # если образ принадлежит классу
                    if cls == target_cls:
                        if res <= 0:
                            success = 0
                            j = 1 / potentials_j[cls]
                            potentials_j[cls] += 1
                            self._potentials[cls].append((j, xk_new))
                        else:
                            success += 1
                    # если образ НЕ принадлежит классу
                    else:
                        if res >= 0:
                            success = 0
                            j = - 1 / potentials_j[cls]
                            potentials_j[cls] += 1
                            self._potentials[cls].append((j, xk_new))
                        else:
                            success += 1

                    print(f'{"*" if success == 0 else ""} #{cls}, K: {res}')
                print()

                if success >= len(images):
                    print(f'Break by success count. Total iterations: {total}')
                    for cls, ph in self._potentials.items():
                        print(cls, ph)
                    print()

                    return total

    def predict(self, image):
        m = 0
        m_cls_idx = 0
        for cls in self.classes:
            k = self.K(image, for_cls=cls)
            if k > m:
                m = k
                m_cls_idx = cls

        return m_cls_idx

    def save(self):
        pass

    @classmethod
    def load(cls):
        pass


class ReStochasticPotentialFieldsClassifier(StochasticPotentialFieldsClassifier):
    """ StochasticModel с переделанным обучением, работает идентично """
    def learn(self, train_data: Dataset.Data, limit=100):
        images = train_data.data
        labels = train_data.labels

        potentials_j = {i: 1 for i in self.classes}
        success = total = 0
        while total < limit:
            print('Global Iteration.')

            total_success = True
            for cls in self.classes:
                total += 1

                for xk_new, target_cls in zip(images, labels):

                    res = self.K(xk_new, for_cls=cls)

                    # если образ принадлежит классу
                    if cls == target_cls:
                        if res <= 0:
                            success = 0
                            total_success = False
                            j = 1 / potentials_j[cls]
                            potentials_j[cls] += 1
                            self._potentials[cls].append((j, xk_new))
                        else:
                            success += 1
                    # если образ НЕ принадлежит классу
                    else:
                        if res >= 0:
                            success = 0
                            total_success = False
                            j = - 1 / potentials_j[cls]
                            potentials_j[cls] += 1
                            self._potentials[cls].append((j, xk_new))
                        else:
                            success += 1

                    print(f'{"*" if success == 0 else ""} #{cls}, K: {res}')
                print()

            if total_success:
                print(f'Break by success count. Total iterations: {total}')
                for cls, ph in self._potentials.items():
                    print(cls, ph)
                print()

                return total
