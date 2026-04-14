from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# токен из Render Environment Variables
TOKEN = os.getenv("TOKEN")

SEND_URL = "https://app.api-messenger.com/sendMessage"

CHAT_LINK_1 = "https://example.com/chat1"
CHAT_LINK_2 = "https://example.com/chat2"

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
                    [
                        {
                            "text": "Дачная, 27",
                            "url": CHAT_LINK_1
                        }
                    ],
                    [
                        {
                            "text": "Красный проспект, 85",
                            "url": CHAT_LINK_2
                        }
                    ]
                ]
            }
        }
    ]

    try:
        requests.post(
            SEND_URL,
            params={"token": TOKEN},
            json=payload,
            timeout=10
        )
    except Exception as e:
        print("SEND ERROR:", e)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("DEBUG:", data)  # важно для проверки структуры MAX

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

# ВАЖНО для Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
