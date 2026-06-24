import pandas as pd

from team_stats import TeamStats


def create_features(df):

    stats = TeamStats(df)

    rows = []

    for _, row in df.iterrows():

        feature_row = stats.build_features(
            row["home_team"],
            row["away_team"]
        )

        rows.append(feature_row)

    return pd.DataFrame(rows)