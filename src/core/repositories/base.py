from typing import Optional, List, Any, Type

from core.databases.sql_connect import BaseModel


class BaseRepository:
    def __init__(self, model: Type[BaseModel]):
        self._model = model

    def list(self, conditions: dict, fields: Optional[list] = None) -> List[Any]:
        query = self._model.select(*(fields or []))
        if conditions:
            query = query.where(**conditions)
        return list(query)

    def first(self, conditions: dict) -> Optional[BaseModel]:
        conditions = (getattr(self._model, key) == value for key, value in conditions.items())
        return self._model.select().where(*conditions).first()

    def create(self, data: dict | List[dict]) -> Optional[BaseModel]:
        if type(data) == list:
            return self._model.insert_many(data).execute()
        return self._model.create(**data)

    def update(self, conditions: dict, data: dict) -> Optional[Any]:
        return self._model.update(**data).where(**conditions)

    def save(self, instance: BaseModel, data: dict) -> BaseModel:
        for key, value in data.items():
            if key not in ["pk", "id", "created_at", "updated_at"]:
                setattr(instance, key, value)
        instance.save()
        return instance

    def delete(self, **kwargs) -> int:
        return self._model.delete().where(**kwargs)
