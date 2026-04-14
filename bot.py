from maxapi import Bot, Dispatcher
from maxapi.types import MessageCreated
import asyncio
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

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
# регистрируем обработчик
dp.add_handler(handle_message)

if __name__ == "__main__":
    dp.run_polling()
