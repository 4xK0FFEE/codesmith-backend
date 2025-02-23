from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.routers.generator.specific import router as SpecificRouter
import src.models.pydantic as models
from src.handlers import GeneratorHandler

router = APIRouter(prefix = "/generate", tags = ["Generator"])

@router.post("/general", tags = ["Generator"])
async def generator_general(input: models.General):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

router.include_router(SpecificRouter)

__all__ = [ "router" ]
