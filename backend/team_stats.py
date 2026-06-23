import pandas as pd


class TeamStats:

    def __init__(self, df):

        self.df = df.copy()

    def get_team_matches(self, team):

        return self.df[
            (self.df["home_team"] == team)
            |
            (self.df["away_team"] == team)
        ]

    def last_n_matches(self, team, n=5):

        matches = self.get_team_matches(team)

        return matches.tail(n)

    def form_points(self, team, n=5):

        matches = self.last_n_matches(team, n)

        points = 0

        for _, row in matches.iterrows():

            if row["home_team"] == team:

                if row["home_goals"] > row["away_goals"]:
                    points += 3

                elif row["home_goals"] == row["away_goals"]:
                    points += 1

            else:

                if row["away_goals"] > row["home_goals"]:
                    points += 3

                elif row["away_goals"] == row["home_goals"]:
                    points += 1

        return points

    def avg_goals_scored(self, team, n=10):

        matches = self.last_n_matches(team, n)

        goals = []

        for _, row in matches.iterrows():

            if row["home_team"] == team:
                goals.append(row["home_goals"])
            else:
                goals.append(row["away_goals"])

        if not goals:
            return 0

        return sum(goals) / len(goals)

    def avg_goals_conceded(self, team, n=10):

        matches = self.last_n_matches(team, n)

        goals = []

        for _, row in matches.iterrows():

            if row["home_team"] == team:
                goals.append(row["away_goals"])
            else:
                goals.append(row["home_goals"])

        if not goals:
            return 0

        return sum(goals) / len(goals)

    def clean_sheet_rate(self, team, n=10):

        matches = self.last_n_matches(team, n)

        clean_sheets = 0

        total = len(matches)

        if total == 0:
            return 0

        for _, row in matches.iterrows():

            if row["home_team"] == team:

                if row["away_goals"] == 0:
                    clean_sheets += 1

            else:

                if row["home_goals"] == 0:
                    clean_sheets += 1

        return clean_sheets / total

    def btts_rate(self, team, n=10):

        matches = self.last_n_matches(team, n)

        total = len(matches)

        if total == 0:
            return 0

        btts = 0

        for _, row in matches.iterrows():

            if (
                row["home_goals"] > 0
                and
                row["away_goals"] > 0
            ):
                btts += 1

        return btts / total

    def over25_rate(self, team, n=10):

        matches = self.last_n_matches(team, n)

        total = len(matches)

        if total == 0:
            return 0

        over25 = 0

        for _, row in matches.iterrows():

            total_goals = (
                row["home_goals"]
                +
                row["away_goals"]
            )

            if total_goals > 2:
                over25 += 1

        return over25 / total

    def build_features(
        self,
        home_team,
        away_team
    ):

        return {

            "home_form":
                self.form_points(home_team),

            "away_form":
                self.form_points(away_team),

            "home_avg_scored":
                self.avg_goals_scored(home_team),

            "away_avg_scored":
                self.avg_goals_scored(away_team),

            "home_avg_conceded":
                self.avg_goals_conceded(home_team),

            "away_avg_conceded":
                self.avg_goals_conceded(away_team),

            "home_clean_sheet_rate":
                self.clean_sheet_rate(home_team),

            "away_clean_sheet_rate":
                self.clean_sheet_rate(away_team),

            "home_btts_rate":
                self.btts_rate(home_team),

            "away_btts_rate":
                self.btts_rate(away_team),

            "home_over25_rate":
                self.over25_rate(home_team),

            "away_over25_rate":
                self.over25_rate(away_team)

        }