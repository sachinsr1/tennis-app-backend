import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Make sure you set your Sportradar API key in your environment
# export SPORTRADAR_API_KEY="your_api_key_here"
API_KEY = os.getenv("SPORTRADAR_API_KEY")

@app.route("/")
def home():
    return jsonify({"message": "Tennis App Backend Running!"})

@app.route("/live-scores")
def live_scores():
    """
    Fetch live summaries of tennis matches from Sportradar.
    Returns JSON to frontend.
    """
    url = "https://api.sportradar.com/tennis/trial/v3/en/sport_events/sr:sport_event:51041587/summary.json"
    params = {"api_key": "X7HcciRhhLIAynD3uVSjKupw1wQ7nWMDdOYBjexC"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises error for 4xx/5xx
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)


"""
{
      "competition_id": "sr:competition:2579",
      "end_date": "2025-06-08",
      "id": "sr:season:119469",
      "name": "French Open Men Singles 2025",
      "start_date": "2025-05-19",
      "year": "2025"
    },
"""
