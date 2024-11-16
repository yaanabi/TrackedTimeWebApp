from abc import ABC, abstractmethod
from typing import Any, List
import pydantic


class BaseRepository(ABC):

    @abstractmethod
    async def get_by_id(self, id: str) -> pydantic.BaseModel:
        pass

    @abstractmethod
    async def get_all(self, limit: int = 100) -> List[pydantic.BaseModel]:
        pass

    @abstractmethod
    async def update(self, id: str, data: pydantic.BaseModel) -> pydantic.BaseModel:
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
