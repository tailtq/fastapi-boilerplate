import os

DATABASE = {
    "engine": os.environ.get("DB_ENGINE", "mysql"),
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "username": os.environ.get("DB_USERNAME", "root"),
    "password": os.environ.get("DB_PASSWORD", "root"),
    "db_name": os.environ.get("DB_NAME", "book_db"),
}
