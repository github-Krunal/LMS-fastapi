from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "dbo"}

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(100))
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    role = Column(String(50), default="student")

    isActive = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)