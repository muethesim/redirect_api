from fastapi import APIRouter
from app.api.v1.api import router as v1_router

router = APIRouter(prefix="/app")

router.include_router(v1_router)
