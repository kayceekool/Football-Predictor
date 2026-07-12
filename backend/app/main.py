from fastapi import FastAPI

from app.init_db import init_db

from app.core.config import settings
from app.core.logging import logger

from app.api.version import router as version_router
from app.api.predictions import router as prediction_router
from app.api.matches import router as match_router
from app.api.health import router as health_router
from app.api.live_predictions import (
    router as live_prediction_router
)

try:
    from app.api.fixtures import router as fixture_router
    logger.info("Fixtures router loaded successfully")
except Exception as e:
    fixture_router = None
    logger.error(f"Fixtures router failed: {e}")

logger.info("Starting Football Predictor AI")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

init_db()

app.include_router(
    version_router,
    prefix="/version",
    tags=["Version"]
)

app.include_router(
    prediction_router,
    prefix="/predictions",
    tags=["Predictions"]
)

app.include_router(
    match_router,
    prefix="/matches",
    tags=["Matches"]
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

if fixture_router:
    app.include_router(
        fixture_router,
        prefix="/fixtures",
        tags=["Fixtures"]
    )

app.include_router(
    live_prediction_router,
    prefix="/live",
    tags=["Live Predictions"]
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }