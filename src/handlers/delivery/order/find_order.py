import asyncio
import itertools

from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.help.getter import FIND_NEW_ORDER
from src.handlers.delivery.order.router import order_router
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@order_router.message(F.text == FIND_NEW_ORDER)
async def find_order(message: types.Message, state: FSMContext) -> None:
    for step in itertools.count():
        if step == settings.MAX_DELIVERY_WAIT_TIME:
            await message.answer('Превышено время ожидания заказа, попробуйте еще раз')
            return

        try:
            data = await do_request(
                f'{settings.TINDER_BACKEND_HOST}/delivery/product/orders',
                method='GET',
            )
        except ClientResponseError:
            await message.answer('Ваш код неверный')
            return

        if order := data['data']:
            await message.answer_photo(
                photo=order['product']['picture_url'],
                caption=render('products/order.jinja2', order=order),
            )
            return

        if step % 50 == 0:
            await message.answer('Пока что нет заказов, ведем поиск...')

        await asyncio.sleep(1)
