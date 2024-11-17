from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from api.v1.router import main_router
from db.mongodb import MongoClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = MongoClient.get_client()
    db = client.get_default_database()
    ping_response = await db.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem connecting to database.")
    else:
        print('Databse connected')
    yield
    MongoClient.close_client()


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
