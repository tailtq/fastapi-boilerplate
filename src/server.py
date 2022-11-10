import dotenv

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

from fastapi import FastAPI

from core.databases.sql_connect import db
import book.controllers.book as book

app = FastAPI()
app.include_router(book.router)


@app.on_event("startup")
def startup():
    db.connect()


@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()
