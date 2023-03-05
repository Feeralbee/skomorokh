"""Processing messages from users"""
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, Text
from src.keyboards.reply import main_menu_keyboard
from src.keyboards.buttons import Buttons
from src.db.connector import Connector
from src.db.queries.users import add_user


async def user_start_handler(message: Message, dbconnector: Connector) -> None:
    """
    This handler receive messages with /start and /help command
    """
    add_user(dbconnector, message.from_user.id, message.from_user.full_name)
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        + "Этот бот может показать вам анекдоты, которые оставили другие пользователи."
        + "Можно также оставлять свои анекдоты",
        reply_markup=main_menu_keyboard(),
    )


async def add_joke_handler(message: Message) -> None:  # pylint: disable=c0116, w0613
    pass  # Need to create add joke handler


async def watch_jokes_handler(message: Message) -> None:  # pylint: disable=c0116, w0613
    pass  # Need to create watch jokes handler


def register_user_handlers(dispatcher: Dispatcher) -> None:
    """Register user message handlers to dispatcher"""
    dispatcher.message.register(user_start_handler, Command(commands=["start", "help"]))
    dispatcher.message.register(
        add_joke_handler, Text(text=str(Buttons.ADD_JOKE.value))
    )
    dispatcher.message.register(
        watch_jokes_handler, Text(text=Buttons.WATCH_JOKES.value)
    )
