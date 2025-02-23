from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src import models
from src.config import Config as config

async def init_db():
    client = AsyncIOMotorClient(config.database)
    config.database_client = client
    await init_beanie(database = client.codesmith, document_models=[ models.General ])
