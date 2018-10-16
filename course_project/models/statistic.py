from peewee import CharField, DateTimeField, PrimaryKeyField, ForeignKeyField
from db import BaseModel
from models.session import Session


class Statistic(BaseModel):
    """ Результат обучения """
    id = PrimaryKeyField()
    name = CharField()

    session = ForeignKeyField(Session)
