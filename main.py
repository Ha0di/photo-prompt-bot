import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_message(message: Message):
    await message.answer("سلام 👋 ربات روشنه و آماده دریافت عکس است.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
