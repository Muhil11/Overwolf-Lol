from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Sample match history (we will replace this with real data)
match_history = pd.DataFrame([
    {"kills": 5, "deaths": 2, "assists": 8, "cs": 150, "win": 1},
    {"kills": 3, "deaths": 5, "assists": 6, "cs": 120, "win": 0},
    {"kills": 8, "deaths": 1, "assists": 10, "cs": 200, "win": 1},
    {"kills": 2, "deaths": 6, "assists": 4, "cs": 100, "win": 0},
])

# AI Model: Predicts win probability based on match stats
def train_model():
    X = match_history.drop(columns=["win"])  # Features
    y = match_history["win"]  # Target (Win or Lose)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)
    
    return model, scaler

model, scaler = train_model()

@app.route("/analyze-match", methods=["POST"])
def analyze_match():
    data = request.json
    input_data = pd.DataFrame([data])

    # Scale the input data
    input_scaled = scaler.transform(input_data)
    win_probability = model.predict(input_scaled)[0]

    # Generate AI suggestions
    suggestions = []
    if data["deaths"] > 5:
        suggestions.append("Try playing safer and avoiding unnecessary fights.")
    if data["cs"] < 150:
        suggestions.append("Improve your creep score for better gold income.")
    if data["kills"] < 3:
        suggestions.append("Focus on better positioning for kill opportunities.")

    return jsonify({
        "win_probability": round(win_probability * 100, 2),
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
