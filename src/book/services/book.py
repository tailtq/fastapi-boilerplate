from fastapi import Depends

from book.repositories.book import BookRepository
from core.services.base import BaseService


class BookService(BaseService):
    a = 5

    def __init__(self, repository: BookRepository = Depends(BookRepository)):
        print(repository.a)
        print("Initialize")
