from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiohttp import ClientResponseError

from src.buttons.help.getter import RANDOM_BUTTON
from src.buttons.products.feedback import get_feedback_buttons
from src.handlers.products.router import products_router
from src.logger import logger
from src.state.login import LoginState
from src.template.render import render
from src.utils.request import do_request

from conf.config import settings


@products_router.message(F.text == RANDOM_BUTTON, LoginState.authorized)
async def start_random(message: types.Message, state: FSMContext) -> None:
    access_token = (await state.get_data())['access_token']

    try:
        data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/product/get_random_product',
            headers={'Authorization': f'Bearer {access_token}'},
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


@products_router.callback_query(F.data == 'like', LoginState.authorized)
async def like_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    await _send_feedback(data['access_token'], data['product_id'], 'liked')

    match callback.message:
        case Message():
            await callback.message.answer(str(data['product_id']))
            await callback.message.delete()


@products_router.callback_query(F.data == 'dislike', LoginState.authorized)
async def dislike_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    # TODO поправь меня
    await _send_feedback(data['access_token'], data['product_id'], 'disliked')

    match callback.message:
        case Message():
            await callback.message.answer(str(data['product_id']))
            await callback.message.delete()


async def _send_feedback(access_token: str, product_id: int, feedback: str) -> None:
    try:
        await do_request(
            f'{settings.TINDER_BACKEND_HOST}/product/feedback',
            headers={'Authorization': f'Bearer {access_token}'},
            params={'product_id': product_id, 'status': feedback},
        )
    except ClientResponseError:
        logger.exception('Error sending feedback')
