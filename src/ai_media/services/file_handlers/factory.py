from core.config import LOCAL_STORAGE_PATH, AWS_PUBLIC_KEY, AWS_SECRET_KEY, AWS_S3_BUCKET
from .local import LocalFileHandler
from .s3 import S3FileHandler
from ai_media.const import FileHandlerType


class FileHandlerFactory:
    def __init__(
        self,
        local_path: str = LOCAL_STORAGE_PATH,
        aws_public_key: str = AWS_PUBLIC_KEY,
        aws_secret_key: str = AWS_SECRET_KEY,
        s3_bucket: str = AWS_S3_BUCKET,
    ):
        self._local_path = local_path
        self._aws_public_key = aws_public_key
        self._aws_secret_key = aws_secret_key
        self._s3_bucket = s3_bucket

    def get_uploader(self, _type: FileHandlerType):
        """
        Factory Pattern to get uploader
        :param _type:
        :return:
        """
        if _type == FileHandlerType.local:
            return LocalFileHandler(self._local_path)
        elif _type == FileHandlerType.s3:
            return S3FileHandler(self._aws_public_key, self._aws_secret_key, self._s3_bucket)
