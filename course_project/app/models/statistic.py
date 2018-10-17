from peewee import CharField, PrimaryKeyField, DoubleField, IntegerField

from app.models.base_model import BaseModel


class Statistic(BaseModel):
    """ Результат обучения """
    id = PrimaryKeyField()
    name = CharField()

    accuracy = DoubleField()  # точность
    fr_accuracy = DoubleField()  # % ошибок первого рода
    sr_accuracy = DoubleField()  # % ошибок второго рода
    learn_time = IntegerField()  # время обучения
