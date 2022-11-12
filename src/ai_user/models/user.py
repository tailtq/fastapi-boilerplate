from peewee import CharField

from core.databases.sql_connect import BaseModel


class User(BaseModel):
    email = CharField(max_length=50)
    password = CharField()
    name = CharField(max_length=100)
