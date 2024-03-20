from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiohttp import ClientResponseError

from src.buttons.help.getter import RANDOM_BUTTON, get_main_keyboard
from src.buttons.products.feedback import get_feedback_buttons
from src.handlers.customer.products.router import products_router
from src.logger import logger
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@products_router.message(F.text == RANDOM_BUTTON)
async def start_random(message: types.Message, state: FSMContext) -> None:
    try:
        data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/customer/product/get_random_product',
        )
    except ClientResponseError:
        await message.answer('Ваш код неверный')
        return

    if product_info := data['data']:
        await state.update_data({'product_id': product_info['id']})

        await message.answer_photo(
            photo=product_info['picture_url'],
            caption=render('products/card.jinja2', product_info=product_info),
            reply_markup=get_feedback_buttons(),
        )
        return

    await message.answer('Нет подборок')
    return


@products_router.callback_query(F.data == 'like')
async def like_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.update_data({'has_already_liked': True})
    await _send_feedback(data['product_id'], 'liked')

    match callback.message:
        case Message():
            await callback.message.answer(
                str(data['product_id']),
                reply_markup=get_main_keyboard(data['role'], has_already_liked=True),
            )
            await callback.message.delete()


@products_router.callback_query(F.data == 'dislike')
async def dislike_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    # TODO поправь меня
    await _send_feedback(data['product_id'], 'disliked')

    match callback.message:
        case Message():
            await callback.message.answer(str(data['product_id']))
            await callback.message.delete()


async def _send_feedback(product_id: int, feedback: str) -> None:
    try:
        await do_request(
            f'{settings.TINDER_BACKEND_HOST}/customer/product/feedback',
            params={'product_id': product_id, 'status': feedback},
        )
    except ClientResponseError:
        logger.exception('Error sending feedback')
