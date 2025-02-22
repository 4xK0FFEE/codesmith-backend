from fastapi import APIRouter, Response
from src.routers.generator.specific import router as SpecificRouter

router = APIRouter(prefix = "/generate", tags = ["Generator"])

@router.post("/general", tags = ["Generator"])
async def generator_general():
    return Response("General Router")

router.include_router(SpecificRouter)

__all__ = [ "router" ]
