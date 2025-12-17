from fastapi import FastAPI
from main.api import item_router

app = FastAPI()


app.include_router(item_router)