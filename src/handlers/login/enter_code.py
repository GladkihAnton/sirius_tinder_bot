from aiogram import types
from aiogram.fsm.context import FSMContext
from aiohttp.client_exceptions import ClientResponseError

from src.buttons.help.getter import get_main_keyboard
from src.handlers.login.router import login_router
from src.logger import logger
from src.state.login import LoginState
from src.utils.request import do_request

from conf.config import settings


@login_router.message(LoginState.enter_code)
async def enter_code(message: types.Message, state: FSMContext) -> None:
    code = message.text
    if message.from_user is None:
        await message.answer('Что-то пошло не так')
        logger.error('Without user')
        return

    try:
        data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/auth/login',
            params={
                'username': message.from_user.id,
                'code': code,
            },
        )
    except ClientResponseError:
        await message.answer('Ваш код неверный')
        return

    data = await state.update_data(data)
    await state.set_state(None)

    await message.answer(
        'Успешно авторизованы',
        reply_markup=get_main_keyboard(data['role'], has_already_liked=data.get('has_already_liked', False)),
    )
