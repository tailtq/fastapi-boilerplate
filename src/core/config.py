import os

from fastapi.security import OAuth2PasswordBearer

DATABASE = {
    "engine": os.environ.get("DB_ENGINE", "mysql"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "username": os.environ.get("DB_USERNAME", "root"),
    "password": os.environ.get("DB_PASSWORD", "root"),
    "db_name": os.environ.get("DB_NAME", "book_db"),
}

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")

JWT_SECRET = os.environ.get("JWT_SECRET", "temporary_secret")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_AUTH_DURATION = int(os.environ.get("JWT_AUTH_DURATION", 86400))
