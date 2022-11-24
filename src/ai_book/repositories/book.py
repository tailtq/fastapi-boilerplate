from typing import Type

from ai_book.models.book import Book
from core.repositories.base import BaseRepository


class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(Book)
