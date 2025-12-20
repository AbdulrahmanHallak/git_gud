import sqlmodel
from fastapi import FastAPI
from src.main.api import item_router
from sqlmodel import SQLModel
app = FastAPI()
app.include_router(item_router)
