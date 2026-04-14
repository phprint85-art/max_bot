from maxapi import Bot
from flask import Flask
import os
import threading
#
#  токен из переменной окружения
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

app = Flask(__name__)

#  фиктивный сервер для Render (порт)
@app.route("/")
def home():
    return "Bot is running"

#  меню (без дублей)
def send_menu(message: Message):
    return message.reply(
        "Выберите филиал:",
        reply_markup={
            "inline_keyboard": [
                [
                    {
                        "text": "Дачная, 27",
                        "url": "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s"
                    }
                ],
                [
                    {
                        "text": "Красный проспект, 85",
                        "url": "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g"
                    }
                ]
            ]
        }
    )

#  /start
@bot.on_command("/start")
async def start(message: Message):
    await send_menu(message)

#  любое сообщение = меню заново
@bot.on_message()
async def any_message(message: Message):
    await send_menu(message)

# запуск Flask (порт Render)
def run_web():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # запускаем порт в фоне
    threading.Thread(target=run_web).start()

    # запускаем бота
    bot.run()
