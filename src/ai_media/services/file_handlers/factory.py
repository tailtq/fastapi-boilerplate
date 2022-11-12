import os

from .local import LocalFileHandler
from .s3 import S3FileHandler
from ai_media.const import FileHandlerType


class FileHandlerFactory:
    def __init__(
        self,
        local_path: str = os.environ.get("LOCAL_STORAGE_PATH"),
        s3_public_key: str = os.environ.get("S3_PUBLIC_KEY"),
        s3_secret_key: str = os.environ.get("S3_SECRET_KEY"),
        s3_bucket: str = os.environ.get("S3_BUCKET"),
    ):
        self._local_path = local_path
        self._s3_public_key = s3_public_key
        self._s3_secret_key = s3_secret_key
        self._s3_bucket = s3_bucket

    def get_uploader(self, _type: FileHandlerType):
        if _type == FileHandlerType.local:
            return LocalFileHandler(self._local_path)
        elif _type == FileHandlerType.s3:
            return S3FileHandler(self._s3_public_key, self._s3_secret_key, self._s3_bucket)
