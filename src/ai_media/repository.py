from typing import Type

from core.repositories.base import BaseRepository
from ai_media.model import Media


class MediaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Media)
