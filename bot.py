from flask import Flask
from maxapi import Bot
import os
import time
import threading

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

app = Flask(__name__)
#
@app.route("/")
def home():
    return "OK"

def debug_loop():
    offset = 0

    print("BOT STARTED")
    print("TOKEN EXISTS:", bool(TOKEN))

    while True:
        try:
            print("REQUESTING UPDATES...")

            updates = bot.get_updates(offset=offset)

            print("RAW UPDATES:", updates)

            if not updates:
                print("NO UPDATES RECEIVED")

            for update in updates:
                print("UPDATE:", update)

                offset = update.get("update_id", offset) + 1

                message = update.get("message")

                if message:
                    chat_id = message["chat"]["id"]
                    print("CHAT ID:", chat_id)

        except Exception as e:
            print("ERROR:", e)

        time.sleep(3)

if __name__ == "__main__":
    threading.Thread(target=debug_loop).start()

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
