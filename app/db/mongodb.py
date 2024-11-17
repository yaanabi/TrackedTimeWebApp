from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGODB_URL


# Maybe rewrite to be compatible with other db's?? But I don't think i will use any other DB so I just leave it as it is rn
class MongoClient:
    _client: AsyncIOMotorClient = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = AsyncIOMotorClient(
                MONGODB_URL
            )  # Getting client doesn't involve async, so no need to await and async def(probably?)
            print('MongoDB client connected')
        return cls._client

    @classmethod
    def close_client(cls):
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            print('MongoDB client disconnected')


CLIENT = MongoClient.get_client()
DATABASE = CLIENT.get_default_database()
