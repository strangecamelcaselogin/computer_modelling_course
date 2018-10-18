from datetime import datetime

from app.models import Session, Scenario


class Model:
    def __init__(self, view):
        self.current_session = None
        self.view = view  # коллбек на обновление данных

    def get_session_by_id(self, id_):
        return Session.get(id=id_)

    def get_sessions(self):
        sessions = Session.select()
        return list(sessions)

    def new_session(self, name):
        s = Session(name=name, creation_date=datetime.now())  # fixme defaults
        s.save(force_insert=True)
        return s

    def set_current_session(self):
        # todo
        pass

    def delete_session(self, name):
        return Session.delete().where(Session.name == name)

    def save_session(self, session, save_as=None):
        if save_as:
            session.name = save_as

        session.save()

        return session

    def get_session_scenarios(self, session: Session):
        scenarios = Scenario.select().where(Scenario.session == session)  # fixme backref

        return list(scenarios)

    def get_scenario(self, id_):
        Scenario.get(id=id_)

    def new_scenario(self, session: Session, name: str):
        scenario = Scenario(name=name, session=session, creation_date=datetime.now())  # fixme defaults

        scenario.save(force_insert=True)

        return scenario

    def update_scenario(self, dataset, features, classifier, statistics):
        # todo
        pass

    def delete_scenario(self, id_):
        Scenario.delete().where(Scenario.id == id_)
