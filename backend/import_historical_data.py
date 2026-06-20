import pandas as pd

from app.database import SessionLocal
from models import Match

df = pd.read_csv(
    "data/matches.csv"
)

db = SessionLocal()

for _, row in df.iterrows():

    match = Match(
        home_team=row["home_team"],
        away_team=row["away_team"],
        home_goals=int(row["home_goals"]),
        away_goals=int(row["away_goals"]),
        match_date=row["date"]
    )

    db.add(match)

db.commit()

db.close()

print(
    "Historical matches imported successfully"
)