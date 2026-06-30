import pandas as pd

from app.services.model_loader import (
    winner_model,
    over15_model,
    over25_model,
    btts_model
)


def predict_match(features):

    X = pd.DataFrame([features])

    winner_probs = winner_model.predict_proba(X)[0]

    over15_prob = (
        over15_model.predict_proba(X)[0][1]
    )

    over25_prob = (
        over25_model.predict_proba(X)[0][1]
    )

    btts_prob = (
        btts_model.predict_proba(X)[0][1]
    )

    winner_index = winner_probs.argmax()

    return {
        "winner": int(winner_index),

        "winner_probability":
            round(
                winner_probs[winner_index] * 100,
                2
            ),

        "over15_probability":
            round(
                over15_prob * 100,
                2
            ),

        "over25_probability":
            round(
                over25_prob * 100,
                2
            ),

        "btts_probability":
            round(
                btts_prob * 100,
                2
            )

WINNERS = {

    0: "Home",

    1: "Draw",

    2: "Away"

}
    }