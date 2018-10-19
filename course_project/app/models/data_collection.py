from datetime import datetime

from peewee import CharField, DateTimeField, PrimaryKeyField, TextField

from app.models.base_model import BaseModel


class DataCollection(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    creation_date = DateTimeField(default=datetime.now)

    learn_data = TextField()  # данные для обучения
    test_data = TextField()  # данные для валидации
