const max = require("@maxhub/max-bot-api");
const http = require("http");

const bot = new max.Bot(process.env.TOKEN);

console.log("BOT STARTED");

let marker = 0;

async function poll() {
    try {
        const updates = await bot.getUpdates();

        console.log("UPDATES:", updates);

        if (updates && updates.length > 0) {
            for (const upd of updates) {

                const msg = upd.message;

                if (msg) {
                    const chatId = msg.chat.id;

                    await bot.sendMessage({
                        chatId: chatId,
                        text: "Выберите филиал:",
                        inline_keyboard: [
                            [{ text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }],
                            [{ text: "Красный проспект, 85", url: "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }]
                        ]
                    });
                }
            }
        }

    } catch (e) {
        console.log("ERROR:", e);
    }

    setTimeout(poll, 3000);
}

poll();

// сервер для Render
http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);
