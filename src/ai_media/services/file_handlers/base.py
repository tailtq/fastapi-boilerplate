from abc import abstractmethod
from typing import BinaryIO


class BaseFileHandler:
    @abstractmethod
    def upload_obj(self, file: BinaryIO, file_name: str):
        pass
