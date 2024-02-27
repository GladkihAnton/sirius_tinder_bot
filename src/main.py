import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from conf.config import settings
from src.db.redis import redis
from src.handlers.login.router import login_router
from src.handlers.main.router import main_router
from src.handlers.products.router import products_router

logging.basicConfig(level=logging.INFO)



def setup_dispatchers(bot: Bot) -> Dispatcher:
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage, bot=bot)

    dp.include_routers(main_router)
    dp.include_routers(login_router)
    dp.include_routers(products_router)

    return dp


async def setup_tg(bot_: Bot, dp_: Dispatcher) -> None:
    logging.info('Setup Telegram')

    webhook = await bot_.get_webhook_info()
    if webhook.url != settings.WEBHOOK_URL:
        logging.info('Delete webhook')
        await bot_.delete_webhook()

    if settings.WEBHOOK_URL:
        logging.info('Set webhook')
        await bot_.set_webhook(settings.WEBHOOK_URL)
    else:
        await dp_.start_polling(bot_)

    logging.info('Finish setup')


bot = Bot(token=settings.BOT_TOKEN)
dp = setup_dispatchers(bot)

if __name__ == "__main__":
    asyncio.run(setup_tg(bot, dp))

