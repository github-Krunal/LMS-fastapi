from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.database import engine, Base, get_db

app = FastAPI()

@app.get("/")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM Users"))
    users = result.fetchall()
    return {"data": [dict(row._mapping) for row in users]}