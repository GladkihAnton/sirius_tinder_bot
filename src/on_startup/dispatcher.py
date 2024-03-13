from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from src.handlers.admin.router import admin_router
from src.handlers.customer.router import customer_router
from src.handlers.delivery.router import delivery_router
from src.handlers.login.router import login_router
from src.handlers.main.router import main_router
from src.integrations.redis import redis
from src.middleware.auth import AuthMiddleware
from src.middleware.logger import LogMessageMiddleware


def setup_dispatcher(bot: Bot) -> Dispatcher:
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage, bot=bot)

    dp.include_routers(main_router)
    dp.include_routers(login_router)

    dp.include_routers(customer_router)
    dp.include_routers(admin_router)
    dp.include_routers(delivery_router)

    dp.message.middleware(LogMessageMiddleware())
    dp.callback_query.middleware(LogMessageMiddleware())

    dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(AuthMiddleware())

    return dp
