from peewee import CharField, DateTimeField, PrimaryKeyField
from db import BaseModel


class DataCollection(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField()

