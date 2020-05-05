from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_URL = "https://www.alphavantage.co/query"

@app.route('/stocks', methods=['GET'])
def get_stocks():
    data = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "IBOV11.SAO",
            "apikey": "Q6G77KV2RXTPJMVK"
            }
    r = requests.get(API_URL, data)
    return r.json()

if __name__ == '__main__':
    app.run(debug=True)