from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from core.dependencies import RepositoryProvider
from repos.trackedtime_repo import TrackedTimeRepository
from schemas.utils_schema import PyObjectId
from schemas.trackedtime_schemas import TrackedTimeIn, TrackedTimeOut

trackedtime_repo = RepositoryProvider('trackedtime').get_repository

router = APIRouter()


@router.get('/{object_id}', response_model=TrackedTimeOut)
async def get_tracked_time(
    object_id: PyObjectId,
    repository: TrackedTimeRepository = Depends(trackedtime_repo)):

    tracked_time = await repository.get_by_id(object_id)
    if not tracked_time:
        raise HTTPException(status_code=404, detail="Tracked time not found")
    return tracked_time


@router.post('/', response_model=TrackedTimeOut)
async def create_tracked_time(
    data: TrackedTimeIn,
    repository: TrackedTimeRepository = Depends(trackedtime_repo)):
    tracked_time = await repository.create(data=data)
    return tracked_time
