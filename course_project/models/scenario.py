from peewee import CharField, PrimaryKeyField, ForeignKeyField, DateTimeField
from db import BaseModel
from models.data_collection import DataCollection
from models.session import Session


class Scenario(BaseModel):
    """ Сценарий - проходит этап выделения признаков, обучение, валидацию """
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField()

    session = ForeignKeyField(Session)
    collection = ForeignKeyField(DataCollection)
    # features = None
    # classifiers = None
