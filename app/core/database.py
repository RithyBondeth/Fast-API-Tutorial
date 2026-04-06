from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import Config

MONGO_URL = Config.MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client["fast_api_tutorial"]
