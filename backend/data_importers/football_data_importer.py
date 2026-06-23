import pandas as pd
import os

LEAGUES = {
    "EPL": "https://www.football-data.co.uk/mmz4281/2425/E0.csv",
    "CHAMPIONSHIP": "https://www.football-data.co.uk/mmz4281/2425/E1.csv",
    "LA_LIGA": "https://www.football-data.co.uk/mmz4281/2425/SP1.csv",
    "SERIE_A": "https://www.football-data.co.uk/mmz4281/2425/I1.csv",
    "BUNDESLIGA": "https://www.football-data.co.uk/mmz4281/2425/D1.csv",
    "LIGUE_1": "https://www.football-data.co.uk/mmz4281/2425/F1.csv"
}

OUTPUT_FILE = "data/all_matches.csv"

all_matches = []

for league, url in LEAGUES.items():

    try:

        print(f"Downloading {league}")

        df = pd.read_csv(url)

        df = df[[
            "Date",
            "HomeTeam",
            "AwayTeam",
            "FTHG",
            "FTAG"
        ]]

        df.columns = [
            "date",
            "home_team",
            "away_team",
            "home_goals",
            "away_goals"
        ]

        all_matches.append(df)

    except Exception as e:

        print(
            f"Failed {league}: {e}"
        )

combined = pd.concat(
    all_matches,
    ignore_index=True
)

combined.to_csv(
    OUTPUT_FILE,
    index=False
)

print(
    f"Saved {len(combined)} matches"
)