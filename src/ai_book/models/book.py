from peewee import *

from core.databases.sql_connect import BaseModel


class Book(BaseModel):
    title = CharField(unique=True)
    description = TextField(default="")
    cover = CharField(default="")
    author = CharField()
    published_at = DateField()

    class Meta:
        table_name = "books"
