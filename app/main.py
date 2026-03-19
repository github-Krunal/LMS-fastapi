from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import engine, Base, get_db
from app.router.v1.router import router_v1
from app.constant.route_constant import VERSION_ONE,API_PREFIX

app = FastAPI()

# router initialization
app.include_router(router_v1, prefix=f"/{API_PREFIX}/{VERSION_ONE}")