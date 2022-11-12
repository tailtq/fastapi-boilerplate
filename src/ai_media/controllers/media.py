from fastapi import APIRouter, UploadFile, File, Depends
from playhouse.shortcuts import model_to_dict

from ai_media.const import FileHandlerType
from ai_media.services.media import MediaService

router = APIRouter(
    prefix="/media",
    tags=["media"],
    dependencies=[]
)


@router.post("/")
async def create(file: UploadFile = File(...), service: MediaService = Depends()):
    file = service.upload_file(file, FileHandlerType.local)
    return model_to_dict(file)
