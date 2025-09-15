from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/tennis/live")
def live_matches():
    url = f"https://api.sportradar.com/tennis/trial/v3/en/schedules/live/summaries.json?api_key={os.getenv('SPORTRADAR_KEY')}"
    r = requests.get(url)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(port=4000, debug=True)
