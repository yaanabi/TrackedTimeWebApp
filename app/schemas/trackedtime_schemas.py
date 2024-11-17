from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from .utils_schema import PyObjectId
from .user_schemas import User
from typing import Dict


class TrackedTime(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    user_id: PyObjectId = Field(
        ..., description='User id related to this tracked time')
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    apps: Dict[str, int] = Field(
        description='Key is app name, value is time tracked in seconds.')

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "user_id": "60f7c2d9fc13ae1b3e000000",
                "created_at": "2024-04-27T12:00:00",
                "apps": {
                    "app1": 123123,
                    "app2": 123213
                }
            }
        }
