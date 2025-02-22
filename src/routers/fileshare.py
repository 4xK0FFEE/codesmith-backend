from fastapi import APIRouter, Response
from src.handlers import FileShareHandler

router = APIRouter(prefix = "/files", tags = ["FileShare Router"])

@router.get("/get")
async def download_file() -> Response:
    return Response("download zip file") # FileResponse
