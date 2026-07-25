from flask import Flask, request, jsonify
import joblib
from flask_cors  import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained ML model
model = joblib.load("ml/predictx_model.pkl")

@app.route("/")
def home():
    return "PredictX API is running!"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    temperature = data["temperature"]
    vibration = data["vibration"]
    pressure = data["pressure"]
    rpm = data["rpm"]
    operating_hours = data["operating_hours"]

    input_data = np.array([[
        temperature,
        vibration,
        pressure,
        rpm,
        operating_hours
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    failure_probability = round(probability * 100, 2)

    if failure_probability < 30:
        risk = "LOW"
        recommendation = "Machine is operating normally."

    elif failure_probability < 70:
        risk = "MEDIUM"
        recommendation = "Schedule a maintenance inspection soon."

    else:
        risk = "HIGH"
        recommendation = "Immediate maintenance inspection recommended."

    return jsonify({
        "failure_prediction": int(prediction),
        "failure_probability": failure_probability,
        "risk_level": risk,
        "recommendation": recommendation
    })


if __name__ == "__main__":
    app.run(debug=True)