import asyncio
import logging

from src.integrations.tg_bot import get_dispatcher, get_tg_bot

logging.basicConfig(level=logging.INFO)


async def start_polling() -> None:
    bot = get_tg_bot()
    dp = get_dispatcher()

    await bot.delete_webhook()
    logging.info('Deleted webhook')

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(start_polling())
