import pandas as pd
import ta

def analyze_indicators(candles):
    df = pd.DataFrame(candles)
    df = df[::-1]

    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['macd'] = ta.trend.MACD(df['close']).macd_diff()
    df['ema'] = ta.trend.EMAIndicator(df['close']).ema_indicator()

    last = df.iloc[-1]
    return f"RSI: {round(last['rsi'], 2)}\nMACD: {round(last['macd'], 4)}\nEMA: {round(last['ema'], 4)}"