from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiohttp import ClientResponseError

from src.buttons.help.getter import CREATE_ORDER
from src.handlers.customer.products.router import products_router
from src.utils.request import do_request

from conf.config import settings


@products_router.message(F.text == CREATE_ORDER)
async def create_order(message: types.Message, state: FSMContext) -> None:
    try:
        await do_request(f'{settings.TINDER_BACKEND_HOST}/customer/product/order')
    except ClientResponseError:
        await message.answer('Ваш код неверный')
        return

    await message.answer('Ваш заказ создан')
