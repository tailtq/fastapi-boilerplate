from typing import Type

from book.models.book import Book
from core.repositories.base import BaseRepository


class BookRepository(BaseRepository):
    def __init__(self, model: Type[Book] = Book):
        super().__init__(model)
