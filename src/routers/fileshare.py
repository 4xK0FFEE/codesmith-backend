from fastapi import APIRouter
from fastapi.responses import FileResponse
from src.handlers import FileShareHandler

router = APIRouter(prefix = "/files", tags = ["FileShare"])

@router.get("/download/{id}", tags = ["FileShare"])
async def download_file(id: int) -> FileResponse:
    file = await FileShareHandler.download_file(id)

    if not file or "path" not in file or "filename" not in file:
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path = file['path'],
        media_type = "application/octet-stream",
        filename = file['filename']
    )

__all__ = [ "router" ]
