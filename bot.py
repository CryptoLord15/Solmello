import os
import telebot
from flask import Flask

# --- Telegram Bot Token ---
TOKEN = "7715529165:AAEIhqKB8-TSD_Wy6O7FETwb-fTv_YuShlQ"
bot = telebot.TeleBot(TOKEN)

# --- Flask app to keep Render happy ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# --- Your bot logic ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hey there 👋! Your bot is live on Render 🚀")

# --- Run bot and Flask together ---
if __name__ == "__main__":
    import threading

    # Run the Telegram bot in one thread
    threading.Thread(target=lambda: bot.polling(non_stop=True)).start()

    # Run the Flask app on Render's expected port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)