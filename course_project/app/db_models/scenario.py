import ujson
from datetime import datetime
from enum import IntEnum

from peewee import CharField, PrimaryKeyField, ForeignKeyField, DateTimeField, SmallIntegerField, TextField
from app.db_models.base_model import BaseModel
from app.db_models.data_collection import DataCollection
from app.db_models.session import Session
from app.db_models.statistic import Statistic


class StatusChoices(IntEnum):
    INITIAL = 1
    IN_PROGRESS = 2
    DONE = 3


class JSONField(TextField):
    def db_value(self, value):
        return value if value is None else ujson.dumps(value)

    def python_value(self, value):
        return value if value is None else ujson.loads(value)


class Scenario(BaseModel):
    """ Сценарий - проходит этап выделения признаков, обучение, валидацию """

    class StatusField(SmallIntegerField):
        def db_value(self, value):
            return value.value

        def python_value(self, value):
            return StatusChoices(value)

    id = PrimaryKeyField()
    name = CharField()
    status = StatusField(default=StatusChoices.INITIAL)
    creation_date = DateTimeField(default=datetime.now)

    # ссылка на сессию, которой принадлежит сценарий
    session = ForeignKeyField(Session)

    # ссылка на датасет
    collection = ForeignKeyField(DataCollection)

    # выбранные алгоритмы выделения признаков
    feature_extractors = JSONField(null=True)

    # выбранный классификатор
    classifier = JSONField()

    # ссылка на результаты сценария
    statistic = ForeignKeyField(Statistic, unique=True, null=True)
