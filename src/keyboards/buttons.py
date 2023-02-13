"""Class for containing buttons text"""
from enum import Enum


class Buttons(str, Enum):
    """Enum class of text for butttons"""

    ADD_JOKE = "Добавить анекдот➕"
    WATCH_JOKES = "Смотреть анекдоты👀"
