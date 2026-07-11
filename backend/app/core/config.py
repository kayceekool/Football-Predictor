import os


class Settings:
    APP_NAME = "Football Predictor AI"

    VERSION = "1.0.0"

    DATABASE_URL = os.getenv("DATABASE_URL")

    API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "CHANGE_ME_IN_RENDER"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"


settings = Settings()