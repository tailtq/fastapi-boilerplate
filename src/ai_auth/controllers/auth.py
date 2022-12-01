from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from playhouse.shortcuts import model_to_dict

from ai_auth.middlewares.parse_bearer_token import get_current_user_info
from ai_auth.requests import UserRegisterRequest
from ai_auth.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[]
)


@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends()):
    auth_service.user_type = "user"
    result = auth_service.login(data.username, data.password)
    return result


@router.post("/register")
def register(data: UserRegisterRequest, auth_service: AuthService = Depends()):
    auth_service.user_type = "user"
    result = auth_service.register(data)
    return model_to_dict(result)


@router.get("/profile")
def get_profile(user_info: dict = Depends(get_current_user_info), auth_service: AuthService = Depends()):
    auth_service.user_type = "user"
    result = auth_service.get_profile(user_info["id"])
    return model_to_dict(result)


@router.post("/refresh-token")
def get_profile(user_info: dict = Depends(get_current_user_info), auth_service: AuthService = Depends()):
    auth_service.user_type = "user"
    result = auth_service.refresh_token(user_info["id"])
    return result
