import pandas as pd

from app.services.api_football import get_today_fixtures
from app.services.predictor import predict_match
from score_predictor import predict_score
from team_stats import TeamStats


def generate_today_predictions():

    fixtures = get_today_fixtures()

    if "response" not in fixtures:
        return []

    df = pd.read_csv("data/matches.csv")

    stats = TeamStats(df)

    predictions = []

    for fixture in fixtures["response"]:

        home = fixture["teams"]["home"]["name"]
        away = fixture["teams"]["away"]["name"]

        try:

            features = stats.build_features(
                home,
                away
            )

            result = predict_match(features)

            expected_home = features["home_avg_scored"]
            expected_away = features["away_avg_scored"]

            score_predictions = predict_score(
                expected_home,
                expected_away
            )

            best_score = score_predictions[0][0]

            confidence = round(
                (
                    result["winner_probability"] +
                    result["over15_probability"] +
                    result["over25_probability"] +
                    result["btts_probability"]
                ) / 4,
                1
            )

            predictions.append({

                "match": f"{home} vs {away}",

                "winner": result["winner"],

                "winner_probability":
                    result["winner_probability"],

                "over15":
                    result["over15_probability"] >= 50,

                "over15_probability":
                    result["over15_probability"],

                "over25":
                    result["over25_probability"] >= 50,

                "over25_probability":
                    result["over25_probability"],

                "btts":
                    result["btts_probability"] >= 50,

                "btts_probability":
                    result["btts_probability"],

                "score":
                    best_score,

                "confidence":
                    confidence

            })

        except Exception:

            continue

    return predictions