from peewee import SqliteDatabase

from config import config


db = SqliteDatabase(config.db_path)
