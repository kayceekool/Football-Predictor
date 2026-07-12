from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/")
def version():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION
    }