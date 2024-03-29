import asyncio

from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.help.getter import GET_LIKED_PRODUCTS
from src.buttons.products.feedback import get_feedback_buttons
from src.handlers.customer.products.router import products_router
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@products_router.message(F.text == GET_LIKED_PRODUCTS)
async def get_liked_products(message: types.Message, state: FSMContext) -> None:
    try:
        data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/customer/product/get_liked_product',
        )
    except ClientResponseError:
        await message.answer('Ваш код неверный')
        return

    if product_infos := data['data']:
        for product_info in product_infos:
            await asyncio.sleep(0)

            await message.answer_photo(
                photo=product_info['picture_url'],
                caption=render('products/card.jinja2', product_info=product_info),
                reply_markup=get_feedback_buttons(),
            )
    else:
        await message.answer('Нет подборок')
        return
