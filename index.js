const http = require("http");

const TOKEN = process.env.TOKEN;
let marker = 0;

async function getUpdates() {
    const res = await fetch(`https://platform-api.max.ru/updates?marker=${marker}`, {
        headers: {
            "Authorization": TOKEN
        }
    });

    const data = await res.json();

    if (data.updates && data.updates.length > 0) {

        marker = data.marker;

        for (const upd of data.updates) {

            const msg = upd.message;

            if (msg) {

                await fetch("https://platform-api.max.ru/messages", {
                    method: "POST",
                    headers: {
                        "Authorization": TOKEN,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        chat_id: msg.chat.id,
                        text: "Выберите филиал:",
                        attachments: [{
                            type: "inline_keyboard",
                            payload: {
                                buttons: [
                                    [{ type: "link", text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }],
                                    [{ type: "link", text: "Красный проспект, 85", url: "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }]
                                ]
                            }
                        }]
                    })
                });
            }
        }
    }
}

setInterval(getUpdates, 3000);

// Render keep-alive сервер
http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);
