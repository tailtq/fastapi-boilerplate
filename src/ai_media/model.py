from peewee import CharField, IntegerField

from core.databases.sql_connect import BaseModel


class Media(BaseModel):
    filename = CharField()
    mimetype = CharField()
    size = IntegerField()
    link = CharField()
