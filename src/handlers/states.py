"""States for handlers"""
from dataclasses import dataclass
from aiogram.fsm.state import StatesGroup, State


@dataclass
class AddingJoke(StatesGroup):
    """States for adding joke"""

    inputting_joke_text = State()


@dataclass
class ManagingNewJokes(StatesGroup):
    """States for Managing new joke"""

    joke_id: int
    choosing_an_action = State()
