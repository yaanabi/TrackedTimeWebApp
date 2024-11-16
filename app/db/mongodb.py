from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL

class MongoClient:
    _client: AsyncIOMotorClient = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            _client = AsyncIOMotorClient(MONGODB_URL)
        return _client
            