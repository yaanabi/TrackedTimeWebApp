from bson import ObjectId
from typing import Annotated
from fastapi import Depends


def validate_object_id(object_id: str):
    if not ObjectId.is_valid(object_id):
        raise ValueError('Invalid ObjectId')
    return object_id

PyObjectId = Annotated[str, Depends(validate_object_id)]


