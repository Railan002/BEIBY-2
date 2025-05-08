from flask import Flask, jsonify
import requests
import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(message="Welcome to Betwise Predictions")

@app.route('/predictions')
def predictions():
    # Your prediction logic goes here. You can use your prediction script.
    predictions = {
        "very_high": [
            {"confidence": "90%", "match": "St. Louis City vs Union Omaha", "odds": "1.28", "prediction": "St. Louis City to WIN"},
            {"confidence": "90%", "match": "FC Dallas vs Alta", "odds": "1.12", "prediction": "FC Dallas to WIN"},
            {"confidence": "90%", "match": "Chelsea vs Djurgardens IF", "odds": "1.14", "prediction": "Chelsea to WIN"}
        ],
        "high": [
            {"confidence": "80%", "match": "FAR Rabat vs Moghreb Tetouan", "odds": "1.39", "prediction": "FAR Rabat to WIN"}
        ],
        "medium": [
            {"confidence": "70%", "match": "CS Cartagines vs Sporting San Jose", "odds": "1.42", "prediction": "CS Cartagines to WIN"}
        ]
    }
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)