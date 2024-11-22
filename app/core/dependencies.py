from db.mongodb import DATABASE
from repos.trackedtime_repo import TrackedTimeMongoRepository

collections = {
    'trackedtime': TrackedTimeMongoRepository(DATABASE['trackedtime']),
}


class RepositoryProvider:

    def __init__(self, collection_name):
        self.collection_name = collection_name

    async def get_repository(self):
        try:
            yield collections[self.collection_name]
        finally:
            pass  # Maybe I will need cleanup
