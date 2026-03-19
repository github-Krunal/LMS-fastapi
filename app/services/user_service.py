from sqlalchemy.orm import Session
from app.model.user import User
from app.schema.user_schema import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        Name=user.name,
        Email=user.email,
        PasswordHash=user.password,
        Role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user