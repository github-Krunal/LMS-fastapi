from fastapi import APIRouter
from app.router.sample_route import router as sample_router

router = APIRouter()

router.include_router(sample_router,prefix="/sample",tags=["sample"])