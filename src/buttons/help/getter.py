from aiogram import types


def get_keyboard() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Подобрать подарок")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb)
