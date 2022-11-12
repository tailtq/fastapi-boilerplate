import datetime as dt
from typing import Type

from peewee import MySQLDatabase, PostgresqlDatabase, Database, Model, DateTimeField, SQL

from ..config import DATABASE


def get_db_engine(engine_type: str) -> Type[Database]:
    if engine_type == "mysql":
        engine = MySQLDatabase
    elif engine_type == "postgresql":
        engine = PostgresqlDatabase
    else:
        raise Exception("Invalid engine type")
    return engine


_db_engine = DATABASE["engine"]
_db_host = DATABASE["host"]
_db_port = DATABASE["port"]
_db_username = DATABASE["username"]
_db_password = DATABASE["password"]
_db_name = DATABASE["db_name"]
_db_engine_class = get_db_engine(_db_engine)

db = _db_engine_class(_db_name, host=_db_host, port=_db_port, user=_db_username, password=_db_password)


class BaseModel(Model):
    created_at = DateTimeField(default=dt.datetime.now)
    updated_at = DateTimeField(default=dt.datetime.now)

    class Meta:
        database = db
