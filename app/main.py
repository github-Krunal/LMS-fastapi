from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import engine, Base, get_db
from app.router.v1.router import router_v1
app = FastAPI()

# ✅ Add version ONLY ONCE here
app.include_router(router_v1, prefix="/api/v1")

@app.get("/")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM Users"))
    users = result.fetchall()
    return {"data": [dict(row._mapping) for row in users]}