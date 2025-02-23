class FileShareHandler:
    @staticmethod
    async def download_file(id: int):
        return { "path": f"/files/{id}.zip", "media_type": "application/octet-stream", "filename": "Project.zip"}


