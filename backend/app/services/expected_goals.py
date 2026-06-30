def expected_goals(features):

    home = (
        features["home_avg_scored"] +
        features["away_avg_conceded"]
    ) / 2

    away = (
        features["away_avg_scored"] +
        features["home_avg_conceded"]
    ) / 2

    return home, away