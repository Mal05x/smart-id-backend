from fastapi import APIRouter
from . import attendance

router = APIRouter()
router.include_router(attendance.router)

