from typing import Callable, ParamSpec

from aiogram import types

CREATE_ORDER = 'Создать заказ'
RANDOM_BUTTON = 'Начать подборку товаров'
GET_LIKED_PRODUCTS = 'Получить лайкнутые товары'
FIND_NEW_ORDER = 'Получить заказ'



P = ParamSpec('P')

def get_main_keyboard(role: str, **kwargs) -> types.ReplyKeyboardMarkup:
    return role_to_keyboard_getter[role](**kwargs)


def _get_keyboard_customer(has_already_liked: bool, **kwargs) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=RANDOM_BUTTON)],
        [types.KeyboardButton(text=GET_LIKED_PRODUCTS)],
    ]
    # TODO исправить на глобальный стейт is_like_product_exists

    if has_already_liked:
        kb.append([types.KeyboardButton(text=CREATE_ORDER)])

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def _get_keyboard_delivery(**kwargs) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=FIND_NEW_ORDER)],
    ]
    # TODO исправить на глобальный стейт is_like_product_exists

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


role_to_keyboard_getter: dict[str, Callable[[P.kwargs], types.ReplyKeyboardMarkup]] = {
    'customer': _get_keyboard_customer,
    'delivery': _get_keyboard_delivery,
    # 'admin': _get_keyboard_admin,
}