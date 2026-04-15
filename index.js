const max = require("@maxhub/max-bot-api");
const http = require("http");

const bot = new max.Bot(process.env.TOKEN);

console.log("BOT STARTED");

const server = http.createServer(async (req, res) => {

    if (req.method === "POST") {
        let body = "";

        req.on("data", chunk => {
            body += chunk.toString();
        });

        req.on("end", async () => {
            try {
                const update = JSON.parse(body);

                console.log("UPDATE:", update);

                const msg = update.message;

                if (msg) {
                    await bot.sendMessage({
                        chatId: msg.chat.id,
                        text: "Выберите филиал:",
                        inline_keyboard: [
                            [{ text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }],
                            [{ text: "Красный проспект, 85", url: "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }]
                        ]
                    });
                }

            } catch (e) {
                console.log("ERROR:", e);
            }

            res.end("OK");
        });

    } else {
        res.end("OK");
    }

});

server.listen(process.env.PORT || 3000);
