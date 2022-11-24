import os
from pathlib import Path

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

PROJECT_ROOT_PATH = Path(__file__).parent.parent.parent

JWT_SECRET = os.environ.get("JWT_SECRET", "temporary_secret")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_AUTH_DURATION = int(os.environ.get("JWT_AUTH_DURATION", 86400))

LOCAL_STORAGE_PATH = PROJECT_ROOT_PATH / "src" / os.environ.get("LOCAL_STORAGE_PATH", "./temp")
AWS_PUBLIC_KEY = os.environ.get("AWS_PUBLIC_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_S3_BUCKET = os.environ.get("AWS_S3_BUCKET")
