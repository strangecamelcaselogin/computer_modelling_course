from functools import wraps

import ujson as ujson

from app.models import Session, Scenario, DataCollection


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

    def get_current_scenarios(self):
        if self._current_session is None:
            return

        scenarios = Scenario.select().where(Scenario.session == self._current_session)  # fixme backref

        return list(scenarios)

    def get_scenario(self, id_):
        Scenario.get(id=id_)

    @update_view
    def new_scenario(self, name: str):
        if self._current_session is None:
            return

        scenario = Scenario(name=name, session=self._current_session)

        scenario.save(force_insert=True)

        return scenario

    def update_scenario(self, dataset, features, classifier, statistics):
        # todo
        pass

    def delete_scenario(self, id_):
        return Scenario.delete().where(Scenario.id == id_)

    def new_data_collection(self, name, learn_data, test_data):
        dc = DataCollection(
            name=name,
            learn_data=ujson.dumps(learn_data),
            test_data=ujson.dumps(test_data)
        )

        dc.save(force_insert=True)

        return dc
