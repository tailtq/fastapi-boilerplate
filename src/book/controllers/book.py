from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[]
)


@router.get("/")
async def get_list():
    return []


@router.get("/{book_id}")
async def read(book_id: int):
    return book_id
