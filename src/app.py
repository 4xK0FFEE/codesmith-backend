from fastapi import FastAPI, Response, Request, Cookie
from fastapi.responses import FileResponse,JSONResponse
from fastapi.middleware.cors import CORSMiddleware
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

@app.on_event("shutdown")
def shutdown():
    print("Stopping Server and Workers",flush=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
