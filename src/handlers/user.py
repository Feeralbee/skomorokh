"""User message hanglers"""
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, Text
from src.keyboards import reply
from src.keyboards.buttons import Buttons


async def user_start_handler(message: Message) -> None:
    """
    This handler receive messages with /start command
    """
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"  # type: ignore[union-attr]
        + "Этот бот может показать вам анекдоты, которые оставили другие пользователи."
        + "Можно также оставлять свои анекдоты",
        reply_markup=reply.main_menu_keyboard(),
    )


async def add_joke_handler(message: Message) -> None:  # pylint: disable=c0116, w0613
    pass  # Need to create add joke handler


async def watch_jokes_handler(message: Message) -> None:  # pylint: disable=c0116, w0613
    pass  # Need to create watch jokes handler


def register_user_handlers(dispatcher: Dispatcher) -> None:
    """Register user message handlers to dispatcher"""
    dispatcher.message.register(user_start_handler, Command(commands=["start"]))
    dispatcher.message.register(
        add_joke_handler, Text(text=str(Buttons.ADD_JOKE.value))
    )
    dispatcher.message.register(
        watch_jokes_handler, Text(text=Buttons.WATCH_JOKES.value)
    )
