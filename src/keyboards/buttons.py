"""Class for containing buttons text"""
from enum import Enum


class Buttons(str, Enum):
    """Enum class of text for virtual keyboards buttons"""

    ADD_JOKE = "Добавить анекдот \U00002795"
    WATCH_JOKES = "Смотреть анекдоты \U0001F440"
    CANCEL = "Отмена \U0000274C"
    CHECK_MARK_BUTTON = "\U00002705"
    CROSS_MARK_BUTTON = "\U0000274C"
