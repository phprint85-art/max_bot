const { Bot } = require("@maxhub/max-bot-api");
const http = require("http");

const bot = new Bot(process.env.TOKEN);

// любое сообщение → меню выбора филиала
bot.on("message_created", async (ctx) => {
    await ctx.reply({
        text: "Выберите филиал:",
        inline_keyboard: [
            [{ text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }],
            [{ text: "Красный проспект, 85", url: "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }]
        ]
    });
});

bot.start();

console.log("BOT STARTED");

// сервер для Render
http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);
