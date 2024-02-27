import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.help.getter import get_keyboard
from conf.config import settings
from src.handlers.login.router import login_router
from src.state.login import LoginState


@login_router.message(LoginState.enter_code)
async def enter_code(message: types.Message, state: FSMContext):
    code = message.text

    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/auth/login',
                        json={
                            'username': message.from_user.id,
                            'code': code,
                        },
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except ClientResponseError:
            await message.answer("Ваш код неверный")
            return

    access_token = data['access_token']

    await state.set_data({'access_token': access_token})
    await state.set_state(LoginState.authorized)
    await message.answer("Успешно авторизованы", reply_markup=get_keyboard())
