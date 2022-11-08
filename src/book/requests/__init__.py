from datetime import date
from typing import Optional

from pydantic import BaseModel, validator


class CreateBookRequest(BaseModel):
    title: str
    author: str
    published_at: date


class UpdateBookRequest(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_at: Optional[date]

    @validator("title", "published_at")
    def prevent_none(cls, v):
        assert v is not None, "value may not be None"
        return v
