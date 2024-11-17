from .base_repo import BaseRepository
from motor.motor_asyncio import AsyncIOMotorCollection
from schemas.utils_schema import PyObjectId
from asyncio import sleep


class TrackedTimeRepository(BaseRepository):

    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    async def get_by_id(self, object_id: PyObjectId):
        print(object_id)

    async def get_all(self, limit=100):
        pass

    async def update(self, object_id: PyObjectId, data):
        pass

    async def delete(self, object_id: PyObjectId):
        pass
