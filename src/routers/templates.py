from fastapi import APIRouter, Response
from src.handlers import TemplateHandler
from src.handlers import FileShareHandler

router = APIRouter(prefix = "/templates", tags = ["Template Router"])

@router.get("/list")
async def list_templates() -> Response:
    return Response('template list') # JSONResponse

@router.post("/add")
async def add_template() -> Response:
    return Response("template add") # JSONResponse

@router.post("/generate")
async def generate_template() -> Response:
    return Response("template generate") # JSONResponse

