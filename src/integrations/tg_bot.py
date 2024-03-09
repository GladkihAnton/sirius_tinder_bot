from aiogram import Bot, Dispatcher

from src.on_startup.dispatcher import setup_dispatcher

from conf.config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = setup_dispatcher(bot)


def get_dispatcher() -> Dispatcher:
    global dp

    return dp


def get_tg_bot() -> Bot:
    global bot

    return bot
