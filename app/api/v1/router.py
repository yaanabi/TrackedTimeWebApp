from .endpoints import tracked_time, users
from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(tracked_time.router, prefix='/tracked_time', tags=['Tracked Time'])
main_router.include_router(users.router, prefix='/users', tags=['Users'])
