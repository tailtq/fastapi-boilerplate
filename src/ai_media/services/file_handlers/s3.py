from ai_media.services.file_handlers.base import BaseFileHandler


class S3FileHandler(BaseFileHandler):
    def __init__(self, s3_public_key: str, s3_secret_key: str, s3_bucket: str):
        self._s3_public_key = s3_public_key
        self._s3_secret_key = s3_secret_key
        self._s3_bucket = s3_bucket

    def upload_obj(self):
        pass
