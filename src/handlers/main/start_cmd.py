from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.handlers.main.router import main_router
from src.logger import logger


@main_router.message(
    Command(
        'start',
    )
)
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    logger.info('Start cmd')

    await message.answer('Спасибо что пришли')
    return
