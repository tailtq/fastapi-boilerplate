from fastapi import APIRouter, Depends

from book.requests import CreateBookRequest, UpdateBookRequest
from book.services import BookService

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[]
)


@router.get("/")
async def get_list(service: BookService = Depends(BookService)):
    print(service.a)
    return []


@router.get("/{book_id}")
async def read(book_id: int, service: BookService = Depends(BookService)):
    print(service.a)
    return book_id


@router.post("/")
async def create(data: CreateBookRequest):
    print(data)
    book = None
    return book


@router.put("/{book_id}")
async def update(book_id: int, data: UpdateBookRequest):
    book = None
    return book


@router.delete("/{book_id}")
async def delete(book_id: int):
    return True
