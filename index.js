const max = require("@maxhub/max-bot-api");
const http = require("http");

const bot = new max.Bot(process.env.TOKEN);

bot.onAny(async (event) => {
    console.log("EVENT:", JSON.stringify(event, null, 2));
});

bot.start();

http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);
