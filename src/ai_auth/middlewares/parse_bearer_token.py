import jwt
from colorama import Fore
from fastapi import Depends, HTTPException, status

from core.config import OAUTH2_SCHEME, JWT_SECRET, JWT_ALGORITHM


def _parse_bearer_token(token: str):
    try:
        result = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return result
    except Exception as e:
        print(Fore.RED + "JWT Error:", e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid_token")


def get_current_user_info(token: str = Depends(OAUTH2_SCHEME)):
    result = _parse_bearer_token(token)
    return result
