from sqlalchemy.orm import Session
from app.model.user import User
from app.schema.user_schema import UserCreate
from datetime import datetime

def create_user(db: Session, user: UserCreate):
    # ✅ Create user
    db_user = User(
        username=user.username,
        name=user.name,
        email=user.email,
        password=user.password,
        role=user.role,
        created_at=datetime.utcnow()
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user