const http = require("http");

const TOKEN = process.env.TOKEN;
let marker = 0;

async function getUpdates() {
    try {
        const res = await fetch(`https://platform-api.max.ru/updates?marker=${marker}`, {
            headers: {
                "Authorization": TOKEN
            }
        });

        const text = await res.text();

        console.log("RAW RESPONSE:", text);

        const data = JSON.parse(text);

        console.log("PARSED:", data);

        if (data.updates && data.updates.length > 0) {
            marker = data.marker;

            console.log("UPDATES COUNT:", data.updates.length);
        }

    } catch (e) {
        console.log("ERROR:", e);
    }
}

setInterval(getUpdates, 3000);

http.createServer((req, res) => {
    res.end("OK");
}).listen(process.env.PORT || 3000);
