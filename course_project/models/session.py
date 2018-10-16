from peewee import CharField, DateTimeField, PrimaryKeyField
from db import BaseModel


class Session(BaseModel):
    """ Сессия - состоит из множества сценариев """
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField()
