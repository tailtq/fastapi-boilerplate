from typing import Type, Optional

from ai_user.models.user import User
from core.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    @staticmethod
    def get_info_for_jwt_token(user: User) -> dict:
        return {
            "id": user.id,
            "email": user.email,
        }

    def get_profile(self, user: int | User) -> Optional[User]:
        if type(user) == int:
            user = self._model.select().where(User.id == user).first()
            if not user:
                return None
        user.password = None
        return user
