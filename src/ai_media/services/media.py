import datetime

from fastapi import UploadFile, Depends
from slugify import slugify

from ai_media.model import Media
from ai_media.repository import MediaRepository
from core.services.base import BaseService
from ai_media.const import FileHandlerType
from ai_media.services.file_handlers import FileHandlerFactory


class MediaService(BaseService):
    def __init__(self, repository: MediaRepository = Depends(), file_handler_factory: FileHandlerFactory = Depends()):
        super().__init__(repository)
        self._file_handler_factory = file_handler_factory

    def upload_file(self, file: UploadFile, uploader_type: FileHandlerType) -> Media:
        """

        """
        uploader = self._file_handler_factory.get_uploader(uploader_type)
        orig_filename, extension = file.filename.split(".")
        filename = f"{self._get_current_datetime()}_{slugify(orig_filename)}.{extension}"
        link, size = uploader.upload_obj(file.file, filename)

        return self._repository.create({
            "filename": f"{orig_filename}.{extension}",
            "mimetype": file.content_type,
            "size": size,
            "link": link,
        })

    def _delete_relationships(self, _id: str | int):
        pass

    def _get_current_datetime(self) -> str:
        return datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
