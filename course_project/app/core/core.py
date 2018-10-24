from datetime import datetime
from threading import Thread
from typing import List, Optional

from app.core.abstract_feature_extractor import AbstractFeatureExtractor
from app.core.abstract_classifier import AbstractClassifier

from app.core.dataset import Dataset
from app.model import Model
from app.db_models import Scenario, DataCollection
from app.setup import logger


def find_plugin_by_name(abstract_pluggable_cls, plugin_name):
    """ Находит плагин в abstract_pluggable_cls по его имени """
    for plugin_cls in abstract_pluggable_cls.plugins:
        if plugin_cls.__name__ == plugin_name:
            return plugin_cls
    else:
        raise Exception(f'AbstractFeatureExtractor plugin {plugin_name} not found')  # fixme


class SessionProcessor:
    """ Отвечает за процесс обучения и валидации сценариев сессии """
    def __init__(self, model: Model):
        self.model = model

        self._running = False
        self._thread = None

    def start(self):
        """ Запуск обработки сессии """
        if self._running:
            raise Exception("Can not start SessionProcessor - already running")  # fixme

        self._running = True
        self._thread = Thread(target=self._safe_thread_wrapper)
        self._thread.start()

    def stop(self, timeout=60):
        """ Остановка обработки. Прогресс незавершенных сценариев будет утерян """
        if not self._running:
            raise Exception("Can not stop thread - already stopped")  # fixme

        self._running = False
        if self._thread:
            self._thread.join(timeout)

    def _safe_thread_wrapper(self):
        try:
            self._process()
        except Exception as e:
            logger.exception(e)
            # todo send signal?
        finally:
            self._running = False

    def _process(self):
        """
        Тут происходит обработка сценариев сессии:
        Для каждого сценария:
            выбирается связанная коллекция данных
            выбираются связанные плгоритмы выделения признаков
            из датасета формируется новый, состяощий из выделенных признаков
            происходит обучение связанного классификатора
            происходит валидация на test части датасета
            результаты валидации сохраняются в базу
        :return:
        """
        scenarios = self.model.get_scenarios(self.model.current_session)

        while self._running and len(scenarios):
            s = scenarios.pop(0)

            dataset = self._load_dataset(s)

            extractors = self._get_feature_extractors(s)
            if extractors:
                processed_dataset = self._process_dataset(dataset, extractors)
            else:
                processed_dataset = dataset  # todo

            classifier = self._instantiate_classifier(s)  # todo fetch kwargs?

            time = datetime.now()
            classifier.learn(processed_dataset)  # .train_data
            time = datetime.now() - time
            print(f'time: {time}')
            statistics = classifier.validate(processed_dataset)  # .test_data
            # todo save statistics, time
            # todo save_classifier?

    @staticmethod
    def _load_dataset(current_scenario: Scenario) -> Dataset:
        dc: DataCollection = DataCollection.get(id=current_scenario.collection)
        return Dataset.from_binary(dc.data)

    @staticmethod
    def _get_feature_extractors(current_scenario: Scenario) -> Optional[List[type(AbstractFeatureExtractor)]]:
        """ Возвращает список классов feature_extractors, или None, если их нет """
        if current_scenario.feature_extractors is None:
            return None

        result = []
        for fe_name in current_scenario.feature_extractors:
            result.append(find_plugin_by_name(AbstractFeatureExtractor, fe_name))

        return result

    @staticmethod
    def _instantiate_classifier(current_scenario: Scenario, arguments=(), key_arguments=None) -> type(AbstractClassifier):
        """ Создает экземпляр классфиикатора current_scenario.classifier """
        if key_arguments is None:
            key_arguments = {}

        cls = find_plugin_by_name(AbstractClassifier, current_scenario.classifier)
        return cls(*arguments, **key_arguments)

    @staticmethod
    def _process_dataset(dataset: Dataset, feature_extractors: List[AbstractFeatureExtractor]) -> Dataset:
        """ Подготавливает новый датасет на основе dataset, обрабатывая его feature_extractors """
        for fe in feature_extractors:
            print(fe)  # todo

        return dataset  # fixme new Dataset
