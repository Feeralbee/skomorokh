"""Creating inline keyboards"""
from aiogram import types
from src.keyboards.buttons import Buttons


def get_managing_new_jokes_keyboard() -> types.InlineKeyboardMarkup:
    """Creates inline virtual keyboard for admins to managing new jokes"""
    keyboard_buttons = [
        [
            types.InlineKeyboardButton(
                text=Buttons.CHECK_MARK_BUTTON.value, callback_data="approve"
            ),
            types.InlineKeyboardButton(
                text=Buttons.CROSS_MARK_BUTTON.value, callback_data="disapprove"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(
        inline_keyboard=keyboard_buttons,
        resize_keyboard=True,
    )
