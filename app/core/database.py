from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://rithybondeth999:Bondeth%40mongodb2002@dev-cluster.6ttyyls.mongodb.net/?appName=dev-cluster"

client = AsyncIOMotorClient(MONGO_URL)
db = client["fast_api_tutorial"]