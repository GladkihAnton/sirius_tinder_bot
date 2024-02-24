from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_feedback_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="👍",
            callback_data="like",
        ),
        types.InlineKeyboardButton(
            text="👎",
            callback_data="dislike",
        )
    )
    return builder.as_markup()
