from fastapi import FastAPI

from app.init_db import init_db



from app.api.predictions import router as prediction_router

from app.api.matches import router as match_router

from app.api.health import router as health_router



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