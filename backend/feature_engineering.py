 import pandas as pd



def calculate_team_stats(df):



    teams = {}



    for _, row in df.iterrows():



        home = row["home_team"]

        away = row["away_team"]



        if home not in teams:

            teams[home] = {

                "matches": 0,

                "goals_scored": 0,

                "goals_conceded": 0

            }



        if away not in teams:

            teams[away] = {

                "matches": 0,

                "goals_scored": 0,

                "goals_conceded": 0

            }



        teams[home]["matches"] += 1

        teams[away]["matches"] += 1



        teams[home]["goals_scored"] += row["home_goals"]

        teams[home]["goals_conceded"] += row["away_goals"]



        teams[away]["goals_scored"] += row["away_goals"]

        teams[away]["goals_conceded"] += row["home_goals"]



    return teams





def create_features(df):



    stats = calculate_team_stats(df)



    rows = []



    for _, row in df.iterrows():



        home = row["home_team"]

        away = row["away_team"]



        home_avg_scored = (

            stats[home]["goals_scored"]

            /

            max(stats[home]["matches"], 1)

        )



        home_avg_conceded = (

            stats[home]["goals_conceded"]

            /

            max(stats[home]["matches"], 1)

        )



        away_avg_scored = (

            stats[away]["goals_scored"]

            /

            max(stats[away]["matches"], 1)

        )



        away_avg_conceded = (

            stats[away]["goals_conceded"]

            /

            max(stats[away]["matches"], 1)

        )



        rows.append({

            "home_avg_scored": home_avg_scored,

            "home_avg_conceded": home_avg_conceded,

            "away_avg_scored": away_avg_scored,

            "away_avg_conceded": away_avg_conceded

        })



    return pd.DataFrame(rows)