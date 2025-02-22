import motor

class Config:
    database: str
    database_client: motor.motor_asyncio.AsyncIOMotorClient
