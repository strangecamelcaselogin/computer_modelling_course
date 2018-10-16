from peewee import SqliteDatabase, Model

db = SqliteDatabase('base.db')


class BaseModel(Model):
    class Meta:
        database = db
