from fastapi import FastAPI, Response, Request, Cookie
from fastapi.responses import FileResponse,JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router as Router
from src.config import Config as config
import src.database as database
from src.routers import templates
import os

app = FastAPI()
app.include_router(Router)

config.database = os.getenv("MONGO_URI")

#@app.on_event("startup")
#async def startup():
#    await database.init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(templates.router)

@app.get("/")
async def hello() -> Response:
    return Response('hello')
