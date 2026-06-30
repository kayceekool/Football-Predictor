from fastapi import FastAPI

from app.init_db import init_db

from app.api.predictions import router as prediction_router
from app.api.matches import router as match_router
from app.api.health import router as health_router
from app.api.live_predictions import (
    router as live_prediction_router
)

try:
    from app.api.fixtures import router as fixture_router
    print("Fixtures router loaded successfully")
except Exception as e:
    fixture_router = None
    print("Fixtures router failed:", e)

app = FastAPI(
    title="Football Predictor API"
)

init_db()

app.include_router(
    prediction_router,
    prefix="/predictions",
    tags=["predictions"]
)

app.include_router(
    match_router,
    prefix="/matches",
    tags=["matches"]
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["health"]
)

if fixture_router:
    app.include_router(
        fixture_router,
        prefix="/fixtures",
        tags=["fixtures"]
    )

app.include_router(
    live_prediction_router,
    prefix="/live",
    tags=["Live Predictions"]
)

@app.get("/")
def root():
    return {
        "status": "running",
        "routes": [
            str(route.path)
            for route in app.routes
        ]
    }