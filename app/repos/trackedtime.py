from base import BaseRepository
from motor.motor_asyncio import AsyncIOMotorDatabase

class TrackedTimeRepository(BaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.trackedtimes
    
    async def get_by_id(self, id):
        pass

    async def get_all(self, limit = 100):
        pass
    
    async def update(self, id, data):
        pass
    
    async def delete(self, id):
        pass

