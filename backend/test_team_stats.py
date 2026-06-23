import pandas as pd

from team_stats import TeamStats

df = pd.read_csv(
    "data/matches.csv"
)

stats = TeamStats(df)

print(
    stats.build_features(
        "Arsenal",
        "Chelsea"
    )
)