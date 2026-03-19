from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String, unique=True)
    PasswordHash = Column(String)
    Role = Column(String, default="student")
    CreatedAt = Column(DateTime, default=datetime.utcnow)