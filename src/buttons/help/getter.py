from aiogram import types

RANDOM_BUTTON = 'Начать подборку товаров'
GET_LIKED_PRODUCTS = 'Получить лайкнутые товары'


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=RANDOM_BUTTON)],
        [types.KeyboardButton(text=GET_LIKED_PRODUCTS)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)
