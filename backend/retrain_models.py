import os

os.system(
    "python train_winner_model.py"
)

os.system(
    "python train_over15_model.py"
)

os.system(
    "python train_over25_model.py"
)

os.system(
    "python train_btts_model.py"
)

print(
    "All models retrained"
)