import pandas as pd
import joblib

from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from feature_engineering import create_features

df = pd.read_csv("data/matches.csv")

df = create_features(df)

df["btts"] = (
    (df["home_goals"] > 0)
    &
    (df["away_goals"] > 0)
).astype(int)

X = df[[
    "home_goals",
    "away_goals"
]]

y = df["btts"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LGBMClassifier()

model.fit(X_train, y_train)

preds = model.predict(X_test)

print(
    "BTTS Accuracy:",
    accuracy_score(y_test, preds)
)

joblib.dump(
    model,
    "btts_model.pkl"
)

print("btts_model.pkl saved")