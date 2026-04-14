const { Bot } = require('@maxhub/max-bot-api');
const http = require('http');

const bot = new Bot(process.env.TOKEN);

//  бот
bot.on('message', async (msg) => {
    await bot.sendMessage({
        chatId: msg.chat.id,
        text: "Выберите филиал:",
        inline_keyboard: [
            [{ text: "Дачная, 27", url: "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s" }],
            [{ text: "Красный проспект, 85", url: "http://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g" }]
        ]
    });
});

bot.start();

//  порт для Render
const PORT = process.env.PORT || 3000;

http.createServer((req, res) => {
    res.writeHead(200);
    res.end("Bot is running");
}).listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
