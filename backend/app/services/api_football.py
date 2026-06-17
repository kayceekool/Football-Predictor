import requests
import os

API_KEY = os.getenv("API_FOOTBALL_KEY")

BASE_URL = "https://v3.football.api-sports.io"

headers = {
    "x-apisports-key": API_KEY
}

def get_today_fixtures():

    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=headers
    )

    return response.json()