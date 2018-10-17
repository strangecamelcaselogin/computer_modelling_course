from peewee import CharField, PrimaryKeyField, ForeignKeyField, DateTimeField
from app.models.base_model import BaseModel
from app.models.data_collection import DataCollection
from app.models.session import Session
from app.models.statistic import Statistic


class Scenario(BaseModel):
    """ Сценарий - проходит этап выделения признаков, обучение, валидацию """
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField()

    # ссылка на сессию, которой принадлежит сценарий
    session = ForeignKeyField(Session)

    # ссылка на датасет
    collection = ForeignKeyField(DataCollection, null=True)

    # features = None  # выбранные признаки
    # classifiers = None  # выбранный классификатор

    # ссылка на результаты сценария
    statistic = ForeignKeyField(Statistic, unique=True, null=True)
