from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")

SEND_URL = "https://platform-api.max.ru/messages"


CHAT_LINK_1 = "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s"
CHAT_LINK_2 = "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g"


def send_menu(chat_id):
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

    requests.post(
        SEND_URL,
        params={"token": TOKEN},
        json=payload
    )


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # пытаемся достать chat_id (под разные форматы MAX)
    chat_id = None

    try:
        chat_id = data["message"]["recipient"]["chat_id"]
    except:
        pass

    if chat_id:
        send_menu(chat_id)

    return jsonify({"ok": True})


# важно для Render
if __name__ == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
