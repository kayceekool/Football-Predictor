import pandas as pd
import joblib

from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from feature_engineering import create_features

df = pd.read_csv("data/matches.csv")

df = create_features(df)

df["over15"] = (
    df["total_goals"] > 1
).astype(int)

X = df[[
    "home_goals",
    "away_goals"
]]

y = df["over15"]

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
    "Over1.5 Accuracy:",
    accuracy_score(y_test, preds)
)

joblib.dump(
    model,
    "over15_model.pkl"
)

print("over15_model.pkl saved")