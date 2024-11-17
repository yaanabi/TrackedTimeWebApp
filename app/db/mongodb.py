from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGODB_URL, MONGODB_NAME


# Maybe rewrite to be compatible with other db's?? But I don't think i will use any other DB so I just leave it as it is rn
class MongoClient:
    _client: AsyncIOMotorClient = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            _client = AsyncIOMotorClient(MONGODB_URL)
        return _client


CLIENT = MongoClient.get_client()
DATABASE = CLIENT[MONGODB_NAME]
