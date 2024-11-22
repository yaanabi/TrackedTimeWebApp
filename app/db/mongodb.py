from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGODB_URL


# Maybe rewrite to be compatible with other db's?? But I don't think i will use any other DB so I just leave it as it is rn
class MongoClient:
    __client: AsyncIOMotorClient = None
    __instance = None

    # Don't really need instances, bc im using class methods, but just in case added it. Yes its bad practice, YAGNI bla bla, who cares
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            cls.__client = AsyncIOMotorClient(
                MONGODB_URL
            )  # Getting client doesn't involve async, so no need to await and async def(probably?)
            print('MongoDB client connected')
        return cls.__client

    @classmethod
    def close_client(cls):
        if cls.__client is not None:
            cls.__client.close()
            cls.__client = None
            print('MongoDB client disconnected')


CLIENT = MongoClient.get_client()
DATABASE = CLIENT.get_default_database()
