from aiogram import types


RANDOM_BUTTON = 'test'


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=RANDOM_BUTTON)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)
