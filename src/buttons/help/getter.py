from aiogram import types

CREATE_ORDER = 'Создать заказ'
RANDOM_BUTTON = 'Начать подборку товаров'
GET_LIKED_PRODUCTS = 'Получить лайкнутые товары'


def get_main_keyboard(has_already_liked: bool) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=RANDOM_BUTTON)],
        [types.KeyboardButton(text=GET_LIKED_PRODUCTS)],
    ]
    # TODO исправить на глобальный стейт is_like_product_exists

    if has_already_liked:
        kb.append([types.KeyboardButton(text=CREATE_ORDER)])

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
