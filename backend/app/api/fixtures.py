from fastapi import APIRouter
from app.services.api_football import from datetime import date

def get_today_fixtures():
    today = date.today().strftime("%Y-%m-%d")

    response = requests.get(
        f"{BASE_URL}/fixtures?date={today}",
        headers=headers
    )

    return response.json()