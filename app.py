from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)


# -----------------------------------------
# Load Model
# -----------------------------------------

with open(
    "crop_model.pkl",
    "rb"
) as file:

    model_data = pickle.load(file)


model = model_data["model"]

accuracy = model_data["accuracy"]

feature_importance = model_data["feature_importance"]

num_crops = model_data["num_crops"]

dataset_size = model_data["dataset_size"]


# -----------------------------------------
# Home Route
# -----------------------------------------

@app.route(
    "/",
    methods=["GET", "POST"]
)
def home():

    prediction = None

    probability = None

    error = None


    if request.method == "POST":

        try:

            nitrogen = float(
                request.form["nitrogen"]
            )

            phosphorus = float(
                request.form["phosphorus"]
            )

            potassium = float(
                request.form["potassium"]
            )

            temperature = float(
                request.form["temperature"]
            )

            humidity = float(
                request.form["humidity"]
            )

            ph = float(
                request.form["ph"]
            )

            rainfall = float(
                request.form["rainfall"]
            )


            input_data = pd.DataFrame(

                [[
                    nitrogen,
                    phosphorus,
                    potassium,
                    temperature,
                    humidity,
                    ph,
                    rainfall
                ]],

                columns=[

                    "N",
                    "P",
                    "K",
                    "temperature",
                    "humidity",
                    "ph",
                    "rainfall"

                ]

            )


            # Prediction

            prediction = model.predict(
                input_data
            )[0]


            # Probability

            probabilities = model.predict_proba(
                input_data
            )[0]

            probability = round(
                max(probabilities) * 100,
                2
            )


        except Exception as e:

            error = str(e)


    return render_template(

        "index.html",

        prediction=prediction,

        probability=probability,

        accuracy=round(
            accuracy * 100,
            2
        ),

        num_crops=num_crops,

        dataset_size=dataset_size,

        feature_importance=feature_importance,

        error=error

    )


# -----------------------------------------
# Run Application
# -----------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )