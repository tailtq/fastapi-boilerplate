from pathlib import Path

import dotenv
from peewee_migrate import Router

dotenv.load_dotenv("../.env")

from book.models.book import Book
from core.databases.sql_connect import db

migration_dir = Path.cwd() / "src/core/databases/migrations"
router = Router(db, migration_dir)

if __name__ == "__main__":
    # Create migration (Add new model here)
    router.create(auto=[Book])
    # Run migration/migrations
    router.run()