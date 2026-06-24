import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier

from feature_engineering import create_features


df = pd.read_csv("data/matches.csv")


def get_result(row):

    if row["home_goals"] > row["away_goals"]:
        return 0

    elif row["home_goals"] < row["away_goals"]:
        return 2

    return 1


df["result"] = df.apply(
    get_result,
    axis=1
)

X = create_features(df)

y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.03,
    objective="multi:softprob",
    num_class=3
)

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"Winner Accuracy: {accuracy:.4f}"
)

joblib.dump(
    model,
    "winner_model.pkl"
)

print(
    "winner_model.pkl saved"
)