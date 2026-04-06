from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Initialize MongoDB client using the validated settings
client = AsyncIOMotorClient(settings.MONGO_URL)
db = client["fast_api_tutorial"]
