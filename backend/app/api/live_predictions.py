from fastapi import APIRouter

from app.services.live_predictor import (
    generate_today_predictions
)

router = APIRouter()


@router.get("/today")

def today_predictions():

    return generate_today_predictions()