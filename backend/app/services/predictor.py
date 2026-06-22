import joblib
import pandas as pd

winner_model = joblib.load(
    "winner_model.pkl"
)

over15_model = joblib.load(
    "over15_model.pkl"
)

over25_model = joblib.load(
    "over25_model.pkl"
)

btts_model = joblib.load(
    "btts_model.pkl"
)


def predict_match(
    home_avg_scored,
    home_avg_conceded,
    away_avg_scored,
    away_avg_conceded
):

    X = pd.DataFrame([
        {
            "home_avg_scored":
                home_avg_scored,

            "home_avg_conceded":
                home_avg_conceded,

            "away_avg_scored":
                away_avg_scored,

            "away_avg_conceded":
                away_avg_conceded
        }
    ])

    winner = winner_model.predict(X)[0]

    over15 = over15_model.predict(X)[0]

    over25 = over25_model.predict(X)[0]

    btts = btts_model.predict(X)[0]

    return {
        "winner": int(winner),
        "over15": bool(over15),
        "over25": bool(over25),
        "btts": bool(btts)
    }