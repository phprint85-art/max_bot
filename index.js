const http = require("http");

const TOKEN = process.env.TOKEN;

// твой Render URL (ВАЖНО заменить)
const BASE_URL = "https://max-bot-27cr.onrender.com";

let marker = 0;

/**
 * 1. ПОДПИСКА НА СОБЫТИЯ
 * без этого updates всегда пустой
 */
async function subscribe() {
    try {
        const res = await fetch("https://platform-api.max.ru/subscriptions", {
            method: "POST",
            headers: {
                "Authorization": TOKEN,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: BASE_URL,
                update_types: ["message_created"]
            })
        });

        console.log("SUBSCRIBE:", await res.text());

    } catch (e) {
        console.log("SUBSCRIBE ERROR:", e);
    }
}

/**
 * 2. ПОЛЛИНГ UPDATES
 */
async function poll() {
    try {
        const res = await fetch(
            `https://platform-api.max.ru/updates?marker=${marker}`,
            {
                headers: {
                    "Authorization": TOKEN
                }
            }
        );

        const data = await res.json();

        console.log("RAW:", data);

        marker = data.marker;

        if (data.updates && data.updates.length > 0) {

            for (const upd of data.updates) {

                const msg = upd.message;

                if (!msg) continue;

                await sendMessage(msg.chat.id);
            }
        }

    } catch (e) {
        console.log("POLL ERROR:", e);
    }
}

/**
 * 3. ОТПРАВКА СООБЩЕНИЯ С КНОПКАМИ
 */
async function sendMessage(chatId) {
    try {
        const res = await fetch("https://platform-api.max.ru/messages", {
            method: "POST",
            headers: {
                "Authorization": TOKEN,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                chat_id: chatId,
                text: "Выберите филиал:",
                attachments: [
                    {
                        type: "inline_keyboard",
                        payload: {
                            buttons: [
                                [
                                    { type: "link", text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }
                                ],
                                [
                                    { type: "link", text: "Красный проспект, 85", url: "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }
                                ]
                            ]
                        }
                    }
                ]
            })
        });

        console.log("SEND:", await res.text());

    } catch (e) {
        console.log("SEND ERROR:", e);
    }
}

/**
 * 4. СТАРТ
 */
subscribe();
setInterval(poll, 3000);

/**
 * 5. SERVER (Render keep alive)
 */
http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);

console.log("BOT STARTED");
