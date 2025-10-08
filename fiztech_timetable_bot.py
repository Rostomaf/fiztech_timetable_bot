from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os

TOKEN = "8237463893:AAFi3_BPotJyUa9RIRLtVjIGAA4s5wxDnXk"

# Flask для Render
app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    print(f"🌐 Flask listening on port {port}")
    app.run(host="0.0.0.0", port=port)

async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    text = (
        "Посилання:\n"
        "[Матан (лекція)](https://us02web.zoom.us/j/83423050653?pwd=NXd4bm1SU3pXRlZVKzN4QjZxT1JKZz09)\n"
        "[Матан (практика)](https://us02web.zoom.us/j/89229232594?pwd=TjFBRlBpcjRwVzF5S1hLVDZONGg5QT09)\n"
        "[Фізика (лекція)](https://us05web.zoom.us/j/87596624346?pwd=hsHX3fjaqEq2afqd8KvqxbtP8JEvII.1)\n"
        "[Фізика (практика)](https://us05web.zoom.us/j/88902905018?pwd=CoCU2tr9IsmHiV8EqTOdKBwUHlNWda.1)\n"
        "[Фізика (лаби)](http://meet.google.com/oos-ubnm-kas)\n"
        "[Ан.Геометрія (лекція)](https://us04web.zoom.us/j/73743365728?pwd=USHSbmu2Om2ODWYEAdzBEoSJK5214Z.1)\n"
        "[Ан.Геометрія (практика)](https://us04web.zoom.us/j/73743365728?pwd=USHSbmu2Om2ODWYEAdzBEoSJK5214Z.1)\n"
        "[Англійська](https://us04web.zoom.us/j/3515080424?pwd=NHAxRjNQb2RRRXVNdjd0YXZvZEN3QT09)\n"
        "[Осн.Алгоритмізації](https://us05web.zoom.us/j/84393192423?pwd=5Ysrwt4RUNuKKoP7r7RpxX5DzMP7iS.1)\n"
        "[Історія](https://us02web.zoom.us/j/86720069785?pwd=ERCXI55NEmeIVFWPB4EZPuubcb6EyT.1)\n"
    )

    await context.bot.send_message(
        chat_id=chat.id,
        text=text,
        parse_mode="Markdown"
    )

async def main_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("show", show))
    await application.run_polling()

def main():
    # Flask у фоновому потоці
    Thread(target=run_flask, daemon=True).start()
    # Telegram-бот
    asyncio.run(main_bot())

if __name__ == "__main__":
    main()
