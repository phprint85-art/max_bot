from flask import Flask, request, jsonify
from maxapi import Bot, Dispatcher, F
from maxapi.types import MessageCreated
import requests
import logging
import os

app = Flask(__name__)
# токен из Render Environment Variables
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
#SEND_URL = "https://platform-api.max.ru/messages"

CHAT_LINK_1 = "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s"
CHAT_LINK_2 = "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g"

def send_menu(chat_id):
    if not TOKEN:
        print("ERROR: TOKEN is missing")
        return

    payload = [
        {
            "chatId": chat_id,
            "message": {
                "text": "Выберите филиал:",
                "inline_keyboard": [
                    [{"text": "Дачная, 27", "url": CHAT_LINK_1}],
                    [{"text": "Красный проспект, 85", "url": CHAT_LINK_2}]
                ]
            }
        }
    ]

    try:
        response = requests.post(
            SEND_URL,
            json=payload,
            headers={
                "Authorization": TOKEN,
                "Content-Type": "application/json"
            },
            timeout=10
        )

        print("SEND STATUS:", response.status_code)
        print("SEND RESPONSE:", response.text)

    except Exception as e:
        print("SEND ERROR:", e)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("GOT REQUEST:", data)

        chat_id = None

        # безопасное извлечение chat_id
        if isinstance(data, dict):
            message = data.get("message", {})
            recipient = message.get("recipient", {})
            chat_id = recipient.get("chat_id")

        if chat_id:
            send_menu(chat_id)

        return jsonify({"ok": True})

    except Exception as e:
        print("WEBHOOK ERROR:", e)
        return jsonify({"ok": False})

# важно для Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
