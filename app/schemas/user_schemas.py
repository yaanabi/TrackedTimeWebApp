from bson import ObjectId
from pydantic import BaseModel, Field
from .utils_schema import PyObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId)
    username: str
    gmail: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": "60f7c2d9fc13ae1b3e000000",
                "username": "nabi",
                "email": "nabi@example.com"
            }
        }
