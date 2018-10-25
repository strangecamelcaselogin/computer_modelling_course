from datetime import datetime
from threading import Thread
from typing import List, Optional, Type

from app.core.abstract_feature_extractor import AbstractFeatureExtractor
from app.core.abstract_classifier import AbstractClassifier

from app.core.dataset import Dataset
from app.core.protocol import Protocol
from app.model import Model
from app.db_models import Scenario, DataCollection
from app.setup import logger


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
        Тут происходит обработка сценариев сессии.
        Для каждого сценария:
            - выбирается связанная коллекция данных
            - выбираются связанные алгоритмы выделения признаков
            - из датасета формируется новый, состяощий из выделенных признаков
            - происходит обучение связанного классификатора
            - происходит валидация на test части датасета
            - результаты валидации сохраняются в базу
        :return:
        """
        scenarios = self.model.get_scenarios(self.model.current_session)

        while self._running and len(scenarios):
            s = scenarios.pop(0)

            protocol = Protocol(lambda p: print(p.last_message))

            protocol.add_message('Загрузка данных...')
            dataset = self._load_dataset(s)
            protocol.add_message('Загружено.')  # todo детальнее

            protocol.add_message('Загрузка алгоритмов извлечения признаков...')
            extractors = self._get_feature_extractors(s)
            protocol.add_message('Загружено.')  # todo детальнее

            if extractors:
                protocol.add_message('Обработка входных данных алгоритмами извлечения признаков...')
                processed_dataset = self._process_dataset(dataset, extractors)
                protocol.add_message('Признаки извлечены')
            else:
                protocol.add_message('Извлечение признаков не предусмотрено сценарием.')
                processed_dataset = dataset

            protocol.add_message('Создание классификатора...')
            # todo fetch additional kwargs
            classifier = self._instantiate_classifier(s, [], {
                'classes': processed_dataset.classes,
                'sample_dimensions': processed_dataset.sample_dimensions,
                'protocol': protocol
            })

            protocol.add_message('Обучение классификатора...')
            time = datetime.now()
            res = classifier.learn(processed_dataset.train_data)
            time = datetime.now() - time
            protocol.add_message(f'Обучение классификатора завершено, время обучения: {time}')

            protocol.add_message('Начало валидации...')
            e, t = classifier.validate(processed_dataset.test_data)
            protocol.add_message(f'Валидация завершена, ошибок: {e}/{t}')

            protocol.add_message('Сохранение модели...')
            binary_model = classifier.save()
            protocol.add_message('Сохранено.')
            # todo save protocol
            # todo save statistics, time

    @staticmethod
    def _load_dataset(current_scenario: Scenario) -> Dataset:
        dc: DataCollection = DataCollection.get(id=current_scenario.collection)
        return Dataset.from_binary(dc.data)

    def _get_feature_extractors(self, current_scenario: Scenario) -> Optional[List[Type[AbstractFeatureExtractor]]]:
        """ Возвращает список классов feature_extractors, или None, если их нет """
        if current_scenario.feature_extractors is None:
            return None

        result = []
        for fe_name in current_scenario.feature_extractors:
            result.append(self.model.find_plugin_by_name(AbstractFeatureExtractor, fe_name))

        return result

    def _instantiate_classifier(self, current_scenario: Scenario, arguments=(), key_arguments=None) -> AbstractClassifier:
        """ Создает экземпляр классфиикатора current_scenario.classifier """
        if key_arguments is None:
            key_arguments = {}

        cls = self.model.find_plugin_by_name(AbstractClassifier, current_scenario.classifier)
        return cls(*arguments, **key_arguments)

    @staticmethod
    def _process_dataset(dataset: Dataset, feature_extractors: List[Type[AbstractFeatureExtractor]]) -> Dataset:
        """ Подготавливает новый датасет на основе dataset, обрабатывая его feature_extractors """
        for fe in feature_extractors:
            print(fe)  # todo

        return dataset  # fixme new Dataset
