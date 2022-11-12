from pydantic import BaseModel


class UserRegisterRequest(BaseModel):
    username: str
    password: str
    name: str
