import requests
import os

def get_candle_data(symbol):
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={symbol[:3]}&to_symbol={symbol[3:]}&interval=1min&apikey={api_key}&outputsize=compact"
    r = requests.get(url)
    data = r.json()

    try:
        candles = list(data["Time Series FX (1min)"].values())[:20]
        return [
            {
                'open': float(c['1. open']),
                'high': float(c['2. high']),
                'low': float(c['3. low']),
                'close': float(c['4. close'])
            } for c in candles
        ]
    except:
        return None