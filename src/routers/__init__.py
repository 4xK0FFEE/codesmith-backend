from fastapi import APIRouter,Depends, Response
from src.routers.templates import router as TemplateRouter
from src.routers.fileshare import router as FileShareRouter 
from src.routers.generator import router as GeneratorRouter

router = APIRouter(prefix = "/api", tags=["Base Router"])

@router.get("/healthcheck")
async def health_check() -> Response:
    return Response("health check")

router.include_router(TemplateRouter)
router.include_router(FileShareRouter)
router.include_router(GeneratorRouter)

__all__ = [ "router" ]
