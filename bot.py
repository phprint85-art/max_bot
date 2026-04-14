from maxapi import Bot
from maxapi.types import MessageCreated
import os
import asyncio

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

@bot.on(MessageCreated)
async def handle_message(event: MessageCreated):
    chat_id = event.message.chat.id
    
    await bot.send_message(
        chat_id=chat_id,
        text="Выберите филиал:",
        inline_keyboard=[
            [{"text": "Дачная, 27", "url": "https://max.ru/u/f9LHodD0cOICVtjg3UhFdfLtvrcH3SUeaR4e2a7Q2o-eIPbB9KBkJBfPC2s"}],
            [{"text": "Красный проспект, 85", "url": "https://max.ru/u/f9LHodD0cOLpulUfVSlZJfTT-SQqFejmGqTlbzYKjry5cwZ2H2Za-WQh15g"}]
        ]
    )

if __name__ == "__main__":
    bot.run()
