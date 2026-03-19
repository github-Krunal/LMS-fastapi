from fastapi import APIRouter
from app.router.v1.sample_route import router as sample_router
from app.router.v1.user_route import router as user_router

router_v1 = APIRouter()

router_v1.include_router(sample_router)
router_v1.include_router(user_router)