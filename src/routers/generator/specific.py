from fastapi import APIRouter
from fastapi.responses import JSONResponse
import src.models.pydantic as models
from src.handlers import GeneratorHandler

router = APIRouter(tags=["Generator"])

@router.post("/frontend", tags = ["Generator"])
async def generator_frontend(input: models.Frontend):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/backend", tags = ["Generator"])
async def generator_backend(input: models.Backend ):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/fullstack", tags = ["Generator"])
async def generator_fullstack(input: models.FullStack):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/cli", tags = ["Generator"])
async def generator_cli(input: models.CLI):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/mobile", tags = ["Generator"])
async def generator_mobile(input: models.Mobile):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/ai-ml", tags = ["Generator"])
async def generator_ai_ml(input: models.AiMl):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/game-dev", tags = ["Generator"])
async def generator_game(input: models.GameDev):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

@router.post("/devops", tags = ["Generator"])
async def generator_devops(input: models.DevOps):
    return JSONResponse({"download_link":await GeneratorHandler.generate_file(input)})

__all__ = [ "router" ]
