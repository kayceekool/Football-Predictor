from scipy.stats import poisson

def predict_score(
    expected_home_goals,
    expected_away_goals
):

    scores = []

    for home in range(6):

        for away in range(6):

            probability = (
                poisson.pmf(
                    home,
                    expected_home_goals
                )
                *
                poisson.pmf(
                    away,
                    expected_away_goals
                )
            )

            scores.append(
                (
                    f"{home}-{away}",
                    probability
                )
            )

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scores[:5]


if __name__ == "__main__":

    results = predict_score(
        1.8,
        1.1
    )

    for score in results:

        print(score)