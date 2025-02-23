from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.routers.templates import router as TemplateRouter
from src.routers.fileshare import router as FileShareRouter 
from src.routers.generator import router as GeneratorRouter
from src.config import Config as config
import pymongo

router = APIRouter(prefix = "/api")

@router.get("/healthcheck", tags = ["Base Router"])
async def health_check() -> JSONResponse:
    try:
        await config.database_client.db_name.command("ping")
        return JSONResponse({"status":"ok","database":"connected"}) 
    except pymongo.errors.ServerSelectionTimeoutError:
        return JSONResponse({"status":"error","database":"no server is found"})
    except pymongo.errors.WTimeoutError:
        return JSONResponse({"status":"error","database":"operation timed out"})
    
router.include_router(TemplateRouter)
router.include_router(FileShareRouter)
router.include_router(GeneratorRouter)

__all__ = [ "router" ]
