import requests
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

DEX_API_URL = "https://api.dexscreener.com/latest/dex/tokens/9ZxaJ6XiTEJ3KTQTxokHK4Ekg9MAdxxLNfxScXQfpump"

BOT_TOKEN = "7715529165:AAEIhqKB8-TSD_Wy6O7FETwb-fTv_YuShlQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey bro 😎, I’m your crypto forecast bot! Use /price or /forecast")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(DEX_API_URL)
    data = response.json()

    if 'pairs' in data and len(data['pairs']) > 0:
        pair = data['pairs'][0]
        symbol = pair['baseToken']['symbol']
        price_usd = pair['priceUsd']
        volume = pair['volume']['h24']
        change = pair['priceChange']['h24']

        message = f"""
💰 *{symbol} LIVE UPDATE* 💰
Price: ${price_usd}
24h Volume: ${volume}
24h Change: {change}%
"""
        await update.message.reply_text(message, parse_mode='Markdown')
    else:
        await update.message.reply_text("Coin not found yet bro 😅")

async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    forecasts = [
        "📈 Chart looks bullish today!",
        "⚠️ Might dip soon, trade safe bro!",
        "🚀 This one’s heating up fast!",
        "😴 Market quiet now, but volume rising soon!"
    ]
    await update.message.reply_text(random.choice(forecasts))

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("forecast", forecast))

print("Bot running...")

app.run_polling()
