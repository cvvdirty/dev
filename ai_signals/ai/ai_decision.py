def ai_decision(signal_info):
    lines = signal_info.split('\n')
    rsi = float(lines[0].split(':')[1])
    macd = float(lines[1].split(':')[1])
    ema = float(lines[2].split(':')[1])

    if rsi > 70 and macd < 0:
        return "Перекуплен — SELL 📉"
    elif rsi < 30 and macd > 0:
        return "Перепродан — BUY 📈"
    elif macd > 0 and ema < macd:
        return "Рост продолжается — BUY ✅"
    elif macd < 0 and ema > macd:
        return "Падение вероятно — SELL ⚠️"
    else:
        return "Нет чётких сигналов — ⏸"