"""Create keyboards"""
from aiogram import types
from src.keyboards.buttons import Buttons


def main_menu_keyboard() -> types.ReplyKeyboardMarkup:
    """Creates the main menu virtual reply keyboard"""
    keyboard_buttons = [
        [types.KeyboardButton(text=Buttons.ADD_JOKE.value)],
        [types.KeyboardButton(text=Buttons.WATCH_JOKES.value)],
    ]
    return types.ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие",
    )


def adding_joke_keyboard() -> types.ReplyKeyboardMarkup:
    """Creates virtual reply keyboard with button cancel"""
    keyboard_buttons = [[types.KeyboardButton(text=Buttons.CANCEL.value)]]
    return types.ReplyKeyboardMarkup(
        keyboard=keyboard_buttons,
        resize_keyboard=True,
        input_field_placeholder="Введите анекдот",
    )
