"""Class for containing buttons text"""
from enum import Enum


class Buttons(str, Enum):
    """Enum class of text for butttons"""

    ADD_JOKE = "Добавить анекдот \U00002795"
    WATCH_JOKES = "Смотреть анекдоты \U0001F440"
    CANCEL = "Отмена \U0000274C"
