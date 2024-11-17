from fastapi import FastAPI
from api.v1.router import main_router


app = FastAPI()
app.include_router(main_router)