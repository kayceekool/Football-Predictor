from scipy.stats import poisson

def predict_score(
    home_xg,
    away_xg
):

    best_score = None
    best_prob = 0

    for h in range(6):
        for a in range(6):

            p = (
                poisson.pmf(h, home_xg)
                *
                poisson.pmf(a, away_xg)
            )

            if p > best_prob:

                best_prob = p
                best_score = f"{h}-{a}"

    return best_score