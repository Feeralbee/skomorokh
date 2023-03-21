"""Class for containing buttons text"""
from enum import Enum


class Buttons(str, Enum):
    """Enum class of text for buttons"""

    ADD_JOKE = "Добавить анекдот \U00002795"
    VIEWING_JOKES = "Показать анекдот \U0001F440"
    CANCEL = "Отмена \U0000274C"
