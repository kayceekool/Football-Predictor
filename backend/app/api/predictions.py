from fastapi import APIRouter

router = APIRouter()

@router.get("/today")
def get_predictions():
    return [
        {
            "match": "Arsenal vs Chelsea",
            "winner": "Arsenal",
            "winner_probability": 72.5,
            "over25": True,
            "over25_probability": 67.8,
            "btts": True,
            "btts_probability": 71.2,
            "score": "2-1",
            "confidence": 81
        }
    ]