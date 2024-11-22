from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List

from .base_repo import BaseRepositoryOperations
from schemas.utils_schema import PyObjectId
from schemas.trackedtime_schemas import TrackedTimeOut, TrackedTimeIn


class TrackedTimeMongoRepository(BaseRepositoryOperations):

    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    async def get_by_id(self, object_id: PyObjectId) -> TrackedTimeOut:
        '''
        Get trackedtime document by object id
        '''
        return await self._collection.find_one({'_id': object_id})

    async def get_all(self,
                      user_id: PyObjectId,
                      limit=100) -> List[TrackedTimeOut]:
        '''
        Get all trackedtime documents for user
        '''
        return await self._collection.find_all({'user_id': user_id})

    async def create(self, data: TrackedTimeIn) -> TrackedTimeOut:
        '''
        Create trackedtime document
        '''
        # TODO: Add user_id
        document = data.model_dump(by_alias=True)
        # document['user_id'] = user_id
        document = TrackedTimeOut(**document).model_dump(by_alias=True)
        result = await self._collection.insert_one(document)
        if not result.acknowledged:
            return None
        return await self.get_by_id(document['_id'])

    async def update(self, object_id: PyObjectId, data) -> TrackedTimeOut:
        pass

    async def delete(self, object_id: PyObjectId) -> None:
        pass
