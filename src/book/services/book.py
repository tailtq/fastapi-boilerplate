from typing import Union

from fastapi import Depends

from book.repositories.book import BookRepository
from core.services.base import BaseService


class BookService(BaseService):
    def __init__(self, repository: BookRepository = Depends(BookRepository)):
        super().__init__(repository)
        print("INIT")

    def _delete_relationships(self, _id: Union[str, int]):
        pass
