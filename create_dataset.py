import pandas as pd
import random

random.seed(42)

crops = {
    "rice": {
        "N": (70, 100),
        "P": (35, 60),
        "K": (35, 50),
        "temperature": (20, 30),
        "humidity": (70, 90),
        "ph": (5.5, 7.0),
        "rainfall": (150, 300)
    },
    "maize": {
        "N": (60, 100),
        "P": (35, 60),
        "K": (15, 30),
        "temperature": (18, 27),
        "humidity": (55, 75),
        "ph": (5.5, 7.5),
        "rainfall": (60, 120)
    },
    "chickpea": {
        "N": (20, 50),
        "P": (50, 80),
        "K": (20, 40),
        "temperature": (18, 25),
        "humidity": (20, 40),
        "ph": (6.0, 8.0),
        "rainfall": (60, 100)
    },
    "cotton": {
        "N": (100, 140),
        "P": (35, 60),
        "K": (15, 30),
        "temperature": (22, 35),
        "humidity": (50, 75),
        "ph": (5.5, 7.5),
        "rainfall": (50, 100)
    },
    "wheat": {
        "N": (40, 80),
        "P": (30, 60),
        "K": (20, 40),
        "temperature": (15, 25),
        "humidity": (40, 65),
        "ph": (6.0, 7.5),
        "rainfall": (40, 100)
    },
    "sugarcane": {
        "N": (100, 140),
        "P": (40, 70),
        "K": (40, 70),
        "temperature": (25, 35),
        "humidity": (70, 90),
        "ph": (6.0, 7.5),
        "rainfall": (150, 250)
    }
}

rows = []

for crop, values in crops.items():

    for _ in range(300):

        row = {
            "N": random.uniform(*values["N"]),
            "P": random.uniform(*values["P"]),
            "K": random.uniform(*values["K"]),
            "temperature": random.uniform(*values["temperature"]),
            "humidity": random.uniform(*values["humidity"]),
            "ph": random.uniform(*values["ph"]),
            "rainfall": random.uniform(*values["rainfall"]),
            "label": crop
        }

        rows.append(row)


df = pd.DataFrame(rows)

df.to_csv("Crop_recommendation.csv", index=False)

print("Dataset created successfully!")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())