from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from app.handlers import router

import asyncio

load_dotenv()
API_TOKEN = getenv("TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router) 
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStop!\n")