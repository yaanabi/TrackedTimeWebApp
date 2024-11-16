from db.mongodb import MongoClient
from abc import ABC
from config import MONGODB_NAME


# TODO: make it class based with open-closed principle(To be able to use different repos) and DIP

class BaseRepositoryDependency(ABC):


# async def get_repo():
#     client = MongoClient.get_client()
#     db = client[MONGODB_NAME]
#     repo = 