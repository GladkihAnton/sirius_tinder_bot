import asyncio
import json
import logging
from random import randint


import aiohttp
from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.buttons.help.getter import GET_LIKED_PRODUCTS
from src.buttons.products.feedback import get_feedback_buttons
from conf.config import settings
from src.handlers.login.router import login_router
from src.handlers.products.router import products_router
from src.state.login import LoginState
from src.template.render import render


@products_router.message(F.text == GET_LIKED_PRODUCTS, LoginState.authorized)
async def get_liked_products(message: types.Message, state: FSMContext):
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    access_token = (await state.get_data())['access_token']
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/product/get_liked_product',
                    headers={'Authorization': f'Bearer {access_token}'}
            ) as response:
                response.raise_for_status()
                data = await response.json()
        except aiohttp.ClientResponseError:
            await message.answer("Ваш код неверный")
            return

    if product_infos := data['data']:
        for product_info in product_infos:
            await asyncio.sleep(0)

            await message.answer_photo(
                photo=product_info['picture_url'],
                caption=render('products/card.jinja2', product_info=product_info),
                reply_markup=get_feedback_buttons(),
            )

    return await message.answer('Нет подборок')


async def send_feedback(access_token: str, product_id: int, feedback: str):
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()

    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                    f'{settings.TINDER_BACKEND_HOST}/product/feedback',
                    headers={'Authorization': f'Bearer {access_token}'},
                    params={'product_id': product_id, 'status': feedback}
            ) as response:
                data = await response.json()
                response.raise_for_status()
        except Exception:
            logging.exception(f'Error sending feedback {data}')
