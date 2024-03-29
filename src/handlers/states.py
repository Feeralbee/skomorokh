"""States for handlers"""
from dataclasses import dataclass
from aiogram.fsm.state import StatesGroup, State


@dataclass
class AddingJoke(StatesGroup):
    """States for adding joke"""

    inputting_joke_text = State()
