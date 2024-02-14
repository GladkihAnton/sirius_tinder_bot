from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.handlers.login.router import login_router
from src.state.login import LoginState


@login_router.message(Command("login",))
async def cmd_login(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.enter_code)
    return await message.answer('Введите код')
