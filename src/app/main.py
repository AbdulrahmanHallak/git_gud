from fastapi import FastAPI
from src.app.admin_setup import init_admin

app = FastAPI()
# app.include_router(item_router)
init_admin(app)
