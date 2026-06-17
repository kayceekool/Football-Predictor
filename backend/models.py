from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    fixture_id = Column(Integer, unique=True)

    home_team = Column(String)
    away_team = Column(String)

    home_goals = Column(Integer)
    away_goals = Column(Integer)

    match_date = Column(DateTime)

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)

    fixture_id = Column(Integer)

    home_win_prob = Column(Float)
    draw_prob = Column(Float)
    away_win_prob = Column(Float)

    over25_prob = Column(Float)
    under25_prob = Column(Float)

    btts_yes_prob = Column(Float)
    btts_no_prob = Column(Float)

    predicted_score = Column(String)

    confidence = Column(Float)