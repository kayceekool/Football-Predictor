from fastapi import APIRouter
from app.services.api_football import get_today_fixtures

router = APIRouter()

@router.get("/today")
def today_fixtures():
    return get_today_fixtures()