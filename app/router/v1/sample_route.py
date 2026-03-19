from fastapi import APIRouter

router = APIRouter()

@router.get("/sample")
def home():
    return {"hello": "world"}
