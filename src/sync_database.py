import dotenv
from peewee_migrate import Router

dotenv_path = dotenv.find_dotenv(raise_error_if_not_found=True)
dotenv.load_dotenv(dotenv_path)

from ai_book.models.book import Book
from ai_media.model import Media
from ai_user.models.user import User
from core.databases.sql_connect import db
from core.config import PROJECT_ROOT_PATH

MIGRATION_DIR = PROJECT_ROOT_PATH / "src/core/databases/migrations"

if __name__ == "__main__":
    router = Router(db, MIGRATION_DIR)
    # Create migration (Add new model here)
    router.create(auto=[Book, Media, User])
    # Run migration/migrations
    router.run()
