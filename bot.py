from maxapi import Bot
import os
import time
import threading
from flask import Flask

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "bot is running:

def run_bot():
    offset = 0

    while True:
        try:
             updates = bot.get_updates(offset=offset)

            for update in updates:
                print("UPDATE:", update)

                offset = update["update_id"] + 1

                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]

                bot.send_message(
                    chat_id=chat_id,
                    text="Выберите филиал:",
                    inline_keyboard=[
                        [{"text": "Дачная, 27", "url": "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s"}],
                        [{"text": "Красный проспект, 85", "url": "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g"}]
                    ]
                )

        except Exception as e:
            print("ERROR:", e)

        time.sleep(1)

if __name__ == "__main__":
    treading.Tread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.envirion.get("PORT", 5000)))
