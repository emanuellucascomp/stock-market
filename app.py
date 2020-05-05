from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_URL = "https://www.alphavantage.co/query"

main_stocks_brazil = ["IBOV11.SAO", "ABEV3.SAO", "AZUL4.SAO", "BTOW3.SAO", "B3SA3.SAO", "BBAS3.SAO", "BBSE3.SAO", "BRML3.SAO", "BBDC4.SAO", "LIPR3.SAO"]


@app.route('/search', methods=['GET'])
def search_stock():
    data = {
            "function": "SYMBOL_SEARCH",
            "keywords": request.args['keywords'],
            "apikey": "Q6G77KV2RXTPJMVK"
            }
    r = requests.get(API_URL, data)
    return r.json()


@app.route('/stock', methods=['GET'])
def get_stock():
    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": request.args['symbol'],
        "apikey": "Q6G77KV2RXTPJMVK"
    }
    r = requests.get(API_URL, data)
    return r.json()


if __name__ == '__main__':
    app.run(debug=True)
