import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------------------
# 1. Load Dataset
# -----------------------------------------

data = pd.read_csv("Crop_recommendation.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

print("\nFirst 5 rows:")
print(data.head())


# -----------------------------------------
# 2. Separate Features and Target
# -----------------------------------------

X = data.drop("label", axis=1)

y = data["label"]


# -----------------------------------------
# 3. Split Dataset
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------------------
# 4. Create Random Forest Model
# -----------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# -----------------------------------------
# 5. Train Model
# -----------------------------------------

model.fit(X_train, y_train)

print("\nModel training completed!")


# -----------------------------------------
# 6. Prediction
# -----------------------------------------

y_pred = model.predict(X_test)


# -----------------------------------------
# 7. Accuracy
# -----------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")


# -----------------------------------------
# 8. Classification Report
# -----------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# -----------------------------------------
# 9. Feature Importance
# -----------------------------------------

feature_importance = dict(
    zip(
        X.columns,
        model.feature_importances_
    )
)

print("\nFeature Importance:")

for feature, importance in feature_importance.items():

    print(
        feature,
        ":",
        round(importance, 4)
    )


# -----------------------------------------
# 10. Save Model
# -----------------------------------------

model_data = {

    "model": model,

    "accuracy": accuracy,

    "feature_importance": feature_importance,

    "features": list(X.columns),

    "num_crops": len(y.unique()),

    "dataset_size": len(data)
}


with open(
    "crop_model.pkl",
    "wb"
) as file:

    pickle.dump(
        model_data,
        file
    )


print("\nModel saved successfully!")

print("File: crop_model.pkl")