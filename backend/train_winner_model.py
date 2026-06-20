import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier


# Load historical matches
df = pd.read_csv("data/matches.csv")


# Create target
# 0 = Home Win
# 1 = Draw
# 2 = Away Win

def get_result(row):
    if row["home_goals"] > row["away_goals"]:
        return 0
    elif row["home_goals"] < row["away_goals"]:
        return 2
    return 1


df["result"] = df.apply(get_result, axis=1)


# Simple features for first version
# Later we'll add:
# team strength
# xG
# form
# head-to-head
# league position

X = pd.DataFrame({
    "home_goals": df["home_goals"],
    "away_goals": df["away_goals"]
})

y = df["result"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    objective="multi:softprob",
    num_class=3
)

model.fit(X_train, y_train)


# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.4f}")


# Save model
joblib.dump(
    model,
    "winner_model.pkl"
)

print("winner_model.pkl saved")