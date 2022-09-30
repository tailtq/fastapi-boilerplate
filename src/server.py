from fastapi import FastAPI

from book.controllers import book

app = FastAPI()
app.include_router(book.router)
