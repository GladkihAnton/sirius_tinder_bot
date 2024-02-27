import asyncio

from aiogram import types
from aiogram.fsm.context import FSMContext

from src.handlers.main.router import main_router
from aiogram.filters.command import Command

from src.state.login import LoginState


@main_router.message(Command("start",))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.unauthorized)
    await asyncio.sleep(5)
    await message.answer('Спасибо что пришли')
