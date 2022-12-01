import datetime

import bcrypt
import jwt
from fastapi import Depends, HTTPException
from starlette import status

from ai_auth.requests import UserRegisterRequest
from ai_user.models.user import User
from ai_user.repositories.user import UserRepository
from core.config import JWT_SECRET, JWT_AUTH_DURATION


class AuthService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self._user_repository = user_repository
        self._user_type = ""

    @property
    def user_type(self) -> str:
        return self._user_type

    @user_type.setter
    def user_type(self, user_type: str):
        if user_type not in ["user"]:
            raise ValueError()
        self._user_type = user_type

    @property
    def _repository(self):
        if self._user_type == "user":
            return self._user_repository

    def login(self, username: str, password: str) -> dict:
        """
        :param username:
        :param password:
        :return:
        """
        user = self._repository.first({"email": username})
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid_user")
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid_user")
        info = self._repository.get_info_for_jwt_token(user)
        return {
            **info,
            "token": jwt.encode({
                **info,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_AUTH_DURATION)
            }, JWT_SECRET)
        }

    def register(self, data: UserRegisterRequest) -> User:
        """
        :param data:
        :return:
        """
        user = self._repository.first({"email": data.username})
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="used_email")
        data = {
            "email": data.username,
            "name": data.name,
            "password": bcrypt.hashpw(data.password.encode(), bcrypt.gensalt()),
        }
        user = self._repository.create(data)
        info = self._repository.get_profile(user)
        return info

    def get_profile(self, _id: int) -> User:
        """
        :param _id:
        :return:
        """
        user = self._repository.get_profile(_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid_user")

        return user

    def refresh_token(self, _id: int) -> dict:
        """
        :param _id:
        :return:
        """
        user = self.get_profile(_id)
        return self._generate_token(user)

    def _generate_token(self, user: User) -> dict:
        """
        :param user:
        :return:
        """
        info = self._repository.get_info_for_jwt_token(user)

        return {
            **info,
            "token": jwt.encode({
                **info,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_AUTH_DURATION)
            }, JWT_SECRET)
        }
