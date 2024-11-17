from abc import ABC, abstractmethod
from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
import pydantic


class BaseRepository(ABC):
    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    @abstractmethod
    async def get_by_id(self, id: str) -> pydantic.BaseModel:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100) -> List[pydantic.BaseModel]:
        pass
    
    @abstractmethod
    async def create(self, data: pydantic.BaseModel) -> pydantic.BaseModel:
        pass

    @abstractmethod
    async def update(self, id: str, data: pydantic.BaseModel) -> pydantic.BaseModel:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
