# Чтобы создать новый плагин нужно отнаследовать класс плагина от одного из абстрактных классов
#  Например от AbstractClassifier, реализовать его методы.

# Чтобы подключить новый плагин к системе, необходимо сделать import в этом файле.


# Классификаторы
from plugins.classifiers.potentials_fields.potentials_fields_classifier import PotentialFieldsClassifier
from plugins.classifiers.potentials_fields.stochastic_potentials_fields_classifiers \
    import StochasticPotentialFieldsClassifier, ReStochasticPotentialFieldsClassifier

# Алгоритмы выделения признаков
from plugins.feature_extractors.simple_extractor import SimpleExtractor

# Загрузчики датасетов
from plugins.dataset_loaders.fs_images_loader import FSImagesLoader
from plugins.dataset_loaders.fs_csv_loader import FSCSVLoader
