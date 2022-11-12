from typing import Union

from fastapi import Depends

from ai_book.repositories.book import BookRepository
from core.services.base import BaseService


class BookService(BaseService):
    def __init__(self, repository: BookRepository = Depends(BookRepository)):
        super().__init__(repository)

    def _delete_relationships(self, _id: Union[str, int]):
        pass
