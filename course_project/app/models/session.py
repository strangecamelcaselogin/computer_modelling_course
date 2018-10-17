from peewee import CharField, DateTimeField, PrimaryKeyField
from app.models.base_model import BaseModel


class Session(BaseModel):
    """ Сессия - состоит из множества сценариев """
    id = PrimaryKeyField()
    name = CharField(unique=True)
    creation_date = DateTimeField()
