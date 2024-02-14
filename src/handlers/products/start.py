import aiohttp
from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.buttons.help.getter import RANDOM_BUTTON
from src.conf.config import settings
from src.handlers.login.router import login_router
from src.handlers.products.router import products_router
from src.state.login import LoginState
from src.template.render import render


@products_router.message(F.text == RANDOM_BUTTON, LoginState.authorized)
async def start_random(message: types.Message, state: FSMContext):
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    access_token = (await state.get_data())['access_token']
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/product/get_random_product',
                    headers={'Authorization': f'Bearer {access_token}'}
            ) as response:
                response.raise_for_status()
                data = await response.json()
                print(data)
        except aiohttp.ClientResponseError:
            await message.answer("Ваш код неверный")
            return

    if product_info := data['data']:
        return await message.answer_photo(
            photo=product_info['picture_url'],
            caption=render('products/card.jinja2', product_info=product_info)
        )

    return await message.answer('Нет подборок')
