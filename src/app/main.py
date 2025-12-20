from fastapi import FastAPI
from src.app.api import item_router

app = FastAPI()
app.include_router(item_router)