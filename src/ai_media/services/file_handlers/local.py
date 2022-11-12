import os
from pathlib import Path
from typing import Tuple, BinaryIO

from ai_media.services.file_handlers.base import BaseFileHandler


class LocalFileHandler(BaseFileHandler):
    def __init__(self, local_path: str):
        self._local_path = local_path

    def upload_obj(self, file: BinaryIO, file_name: str) -> Tuple[str, int]:
        """

        """
        if not os.path.exists(self._local_path):
            Path(self._local_path).mkdir(parents=True, exist_ok=True)
        file_path = f"{self._local_path}/{file_name}"
        with open(file_path, "wb") as f:
            content = file.read()
            f.write(content)
            size = f.tell()

        return file_path, size
