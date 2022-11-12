from pathlib import Path

import dotenv
from peewee_migrate import Router

dotenv.load_dotenv(Path(__file__).parent.parent / ".env")

from ai_book.models.book import Book
from ai_media.model import Media
from ai_user.models.user import User
from core.databases.sql_connect import db

migration_dir = Path.cwd() / "src/core/databases/migrations"
router = Router(db, migration_dir)

if __name__ == "__main__":
    # Create migration (Add new model here)
    router.create(auto=[Book, Media, User])
    # Run migration/migrations
    router.run()
