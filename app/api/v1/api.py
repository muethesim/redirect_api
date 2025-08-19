from fastapi import APIRouter
from app.api.v1.compareTo.api import router as compare_to_router
from app.api.v1.inline.api import router as inline_router

router = APIRouter(prefix="/v1")
router.include_router(compare_to_router)
router.include_router(inline_router)
