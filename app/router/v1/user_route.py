from fastapi import APIRouter,Depends
from app.schema.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.user_service import create_user
from app.constant.route_constant import USER_POST_URL

router = APIRouter()

@router.post(USER_POST_URL)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user)
    return {
        "message": "user created successfully",
        "user_id": user.id
    }
