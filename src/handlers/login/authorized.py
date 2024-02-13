from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.help.getter import get_keyboard
from src.handlers.login.router import login_router
from src.state.login import LoginState


@login_router.message(LoginState.authorized)
async def autorized(message: types.Message, state: FSMContext):
    await message.answer("ypa", reply_markup=get_keyboard())
