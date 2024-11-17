from fastapi import APIRouter, Depends

from core.dependencies import RepositoryProvider
from repos.trackedtime_repo import TrackedTimeRepository
from schemas.utils_schema import PyObjectId
from schemas.trackedtime_schemas import TrackedTime

trackedtime_repo = RepositoryProvider('trackedtime').get_repository

router = APIRouter()

@router.get('/{object_id}', response_model=TrackedTime)
async def get_tracked_time(object_id: PyObjectId, repository: TrackedTimeRepository = Depends(trackedtime_repo)):
    try:
        user = await repository.get_by_id(object_id)
        return user
    except Exception as e:
        pass # Add some exception handling
    
@router.post('/', response_model=TrackedTime)
async def create_tracked_time(object_id: PyObjectId, repository: TrackedTimeRepository = Depends(trackedtime_repo)):
    try:
        user = await repository.get_by_id(object_id)
        return user
    except Exception as e:
        pass # Add some exception handling
