import os

import dotenv
import uvicorn
from fastapi import FastAPI

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

from core.databases.sql_connect import db
import ai_book.controllers.book as book
import ai_media.controllers.media as media

app = FastAPI()
app.include_router(book.router)
app.include_router(media.router)


@app.on_event("startup")
def startup():
    db.connect()


@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()


if __name__ == "__main__":
    app_env = os.environ.get("APP_ENV")
    app_port = os.environ.get("APP_PORT", 8000)
    reload = app_env == "local"

    uvicorn.run("server:app", host="0.0.0.0", port=app_port, reload=reload)
