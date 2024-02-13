import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from src.handlers.login.router import login_router
from src.handlers.main.router import main_router

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6883664445:AAH8W_KyWYruMrTI7voBVskEPUeqUP1ccfc')

redis = Redis(
    host='localhost',
    port=6379,
    db=1,
)

storage = RedisStorage(redis)
dp = Dispatcher(storage=storage)

dp.include_routers(main_router)
dp.include_routers(login_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
