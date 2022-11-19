from abc import abstractmethod
from typing import Any, List, Optional

from core.databases.sql_connect import BaseModel
from core.repositories.base import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def list(self, conditions: Optional[dict] = None, fields: Optional[list] = None) -> List[BaseModel]:
        return self._repository.list(conditions or {}, fields)

    def first(self, **kwargs) -> Optional[BaseModel]:
        return self._repository.first(**kwargs)

    def get_by_id(self, _id: Optional[str | int]) -> Optional[BaseModel]:
        return self._repository.first({"id": _id})

    def create(self, data: dict) -> Optional[BaseModel]:
        return self._repository.create(data)

    def update(self, conditions: dict, data: dict) -> Optional[Any]:
        return self._repository.update(conditions, data)

    def save(self, instance: BaseModel, data: dict) -> BaseModel:
        return self._repository.save(instance, data)

    def delete_by_id(self, _id: str | int) -> int:
        self._delete_relationships(_id)
        return self._repository.delete(pk=_id)

    def delete(self, **kwargs) -> int:
        return self._repository.delete(**kwargs)

    @abstractmethod
    def _delete_relationships(self, _id: str | int):
        raise NotImplementedError()
