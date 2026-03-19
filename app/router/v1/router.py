from fastapi import APIRouter
from app.router.v1.sample_route import router as sample_router

router_v1 = APIRouter()

router_v1.include_router(sample_router)
# router.include_router(sample_router,prefix="/api/v1",tags=["user"])