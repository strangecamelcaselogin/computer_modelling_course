from functools import wraps
from pathlib import Path

from typing import List, Optional, Type, TypeVar

from app.core.abstract_classifier import AbstractClassifier
from app.core.abstract_feature_extractor import AbstractFeatureExtractor
from app.core.abstract_dataset_loader import AbstractDatasetLoader

from app.db_models import Session, Scenario, DataCollection
from config import config


def update_view(method):
    """ Обновляет View """
    @wraps(method)
    def decorator(self_, *args, **kwargs):
        result = method(self_, *args, **kwargs)
        if self_.view:
            self_.view.update()
        return result

    return decorator


class Model:
    def __init__(self, view):
        self._current_session = None
        self.view = view  # коллбек на обновление данных

    # Сессии
    def get_session_by_id(self, id_):
        return Session.get(id=id_)

    def get_sessions(self):
        sessions = Session.select()
        return list(sessions)

    @update_view
    def new_session(self, name):
        s = Session(name=name)
        s.save(force_insert=True)
        return s

    @property
    def current_session(self):
        return self._current_session

    @update_view
    def set_current_session(self, session):
        self._current_session = session

    def delete_session(self, name):
        return Session.delete().where(Session.name == name)

    def save_session(self, session, save_as=None):
        if save_as:
            session.name = save_as

        session.save()

        return session

    # Сценарии
    def get_scenarios(self, session: Session) -> List[Scenario]:
        return list(Scenario.select().where(Scenario.session == session))  # fixme backref

    def get_current_scenarios(self) -> Optional[List[Scenario]]:
        if self._current_session is None:
            return

        return self.get_scenarios(self._current_session)

    def get_scenario(self, id_):
        return Scenario.get(id=id_)

    @update_view
    def new_scenario(self, name: str, data_collection: DataCollection, feature_extractors: Optional[List[str]], classifier: str):
        if self._current_session is None:
            return

        scenario = Scenario(
            name=name,
            session=self._current_session,
            collection=data_collection,
            feature_extractors=feature_extractors,
            classifier=classifier
        )

        scenario.save(force_insert=True)

        return scenario

    def update_scenario(self, dataset, features, classifier, statistics):
        raise NotImplementedError

    def delete_scenario(self, id_):
        return Scenario.delete().where(Scenario.id == id_)

    # Датасеты (коллекции)
    def get_data_collections(self):
        return list(DataCollection.select())

    def new_data_collection(self, name: str, path: Path, loader_cls: Type[AbstractDatasetLoader]):
        loader = loader_cls(config.data_path)

        binary_dataset = loader.load(path).as_binary()

        dc = DataCollection(name=name, data=binary_dataset)
        dc.save(force_insert=True)
        return dc

    # Классификаторы
    @staticmethod
    def get_classifiers():
        return AbstractClassifier.plugins

    # FE
    @staticmethod
    def get_feature_extractors():
        return AbstractFeatureExtractor.plugins

    # DatasetLoaders
    @staticmethod
    def get_dataset_loaders():
        return AbstractDatasetLoader.plugins

    # Результаты
    def get_current_results(self):
        raise NotImplementedError

    # ...
    T = TypeVar('T')

    @staticmethod
    def find_plugin_by_name(abstract_pluggable_cls: T, plugin_name) -> Type[T]:
        """ Находит плагин в abstract_pluggable_cls по его имени """
        for plugin_cls in abstract_pluggable_cls.plugins:
            if plugin_cls.__name__ == plugin_name:
                return plugin_cls
        else:
            raise Exception(f'AbstractFeatureExtractor plugin {plugin_name} not found')  # fixme
