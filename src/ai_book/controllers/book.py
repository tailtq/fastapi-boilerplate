from fastapi import APIRouter, Depends
from playhouse.shortcuts import model_to_dict

from ai_book.requests import CreateBookRequest, UpdateBookRequest
from ai_book.services import BookService

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[]
)


@router.get("/")
async def get_list(service: BookService = Depends(use_cache=True)):
    return [model_to_dict(item) for item in service.list()]


@router.get("/{book_id}")
async def read(book_id: int, service: BookService = Depends(use_cache=True)):
    book = service.get_by_id(book_id)
    return model_to_dict(book)


@router.post("/")
async def create(data: CreateBookRequest, service: BookService = Depends(use_cache=True)):
    book = service.create(data.dict())
    return model_to_dict(book)


@router.put("/{book_id}")
async def update(book_id: int, data: UpdateBookRequest):
    book = None
    return book


@router.delete("/{book_id}")
async def delete(book_id: int):
    return True
