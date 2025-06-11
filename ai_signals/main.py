import os
import telebot
from services.fetch_data import get_candle_data
from services.indicators import analyze_indicators
from ai.ai_decision import ai_decision
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

PAIRS = ['EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD', 'USDCAD',
         'NZDUSD', 'EURJPY', 'GBPJPY', 'EURGBP', 'CHFJPY']

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Привет! Напиши /signal, чтобы получить сигнал.")

@bot.message_handler(commands=['signal'])
def signal(message):
    for pair in PAIRS:
        candles = get_candle_data(pair)
        if candles:
            signal_info = analyze_indicators(candles)
            decision = ai_decision(signal_info)
            text = f"🔎 {pair}\n{signal_info}\n💡 AI: {decision}"
            bot.send_message(message.chat.id, text)

bot.polling()