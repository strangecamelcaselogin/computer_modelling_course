from datetime import datetime

from peewee import CharField, DateTimeField, PrimaryKeyField, BlobField

from app.models.base_model import BaseModel


class DataCollection(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField(default=datetime.now)

    learn = BlobField()  # данные для обучения
    validate = BlobField()  # данные для валидации
