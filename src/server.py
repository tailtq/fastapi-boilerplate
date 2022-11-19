import os

import dotenv
import uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError, HTTPException

from core.utils.response_formatter import CustomORJSONResponse

dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

from core.databases.sql_connect import db
import ai_book.controllers.book as book
import ai_media.controllers.media as media
import ai_auth.controllers.auth as auth

app = FastAPI(default_response_class=CustomORJSONResponse)
app.include_router(book.router)
app.include_router(media.router)
app.include_router(auth.router)


@app.on_event("startup")
def startup():
    db.connect()


@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, e: RequestValidationError):
    return CustomORJSONResponse(e.errors(), status.HTTP_400_BAD_REQUEST)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, e: HTTPException):
    return CustomORJSONResponse({"reason": e.detail} if e.detail else None, e.status_code)


if __name__ == "__main__":
    app_env = os.environ.get("APP_ENV")
    app_port = int(os.environ.get("APP_PORT", 8000))
    reload = app_env == "local"

    uvicorn.run("server:app", host="0.0.0.0", port=app_port, reload=reload)
