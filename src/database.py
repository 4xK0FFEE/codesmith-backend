from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from src.models import Template
from src.config import Config as config

async def init_db():
    client = AsyncIOMotorClient(config.database)
    await init_beanie(database = client.codesmith, document_models=[Template])
