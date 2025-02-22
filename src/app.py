from fastapi import FastAPI, Response, Request, Cookie
from fastapi.responses import FileResponse,JSONResponse 
from src.routers import router as Router
from src.config import Config as config
import src.database as database
import os

app = FastAPI()
app.include_router(Router)

config.database = os.getenv("MONGO_URI")

@app.on_event("startup")
async def startup():
    await database.init_db()

@app.get("/")
async def hello() -> Response:
    return Response('hello')
