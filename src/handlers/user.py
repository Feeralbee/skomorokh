"""Processing messages from users"""
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from src.handlers.states import AddingJoke
from src.keyboards.reply import main_menu_keyboard, adding_joke_keyboard
from src.keyboards.buttons import Buttons
from src.db.connector import Connector
from src.db.queries.users import add_user
from src.db.queries.jokes import add_joke


async def user_start_handler(message: Message, dbconnector: Connector) -> None:
    """
    This procedure handles the /start and /help commands
    """
    add_user(dbconnector, message.from_user.id, message.from_user.full_name)
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        + "Этот бот может показать вам анекдоты, которые оставили другие пользователи."
        + "Можно также оставлять свои анекдоты",
        reply_markup=main_menu_keyboard(),
    )


async def add_joke_handler(message: Message, state: FSMContext) -> None:
    """
    This procedure handles "Добавить анекдот" message
    """
    await message.answer(
        "Введите текст анекдота, который хотели бы добавить",
        reply_markup=adding_joke_keyboard(),
    )
    await state.set_state(AddingJoke.inputting_joke_text)


async def joke_was_introduced(
    message: Message, state: FSMContext, dbconnector: Connector
) -> None:
    """Next state adding joke"""
    if message.text == Buttons.CANCEL.value:
        await message.answer("Добавление отменено", reply_markup=main_menu_keyboard())
    else:
        add_joke(dbconnector, message.text, message.from_user.id)
        await message.answer(
            "Анекдот получен и отправлен на проверку", reply_markup=main_menu_keyboard()
        )
    await state.clear()


async def watch_jokes_handler(message: Message) -> None:  # pylint: disable=c0116, w0613
    pass  # Need to create watch jokes handler


def register_user_handlers(dispatcher: Dispatcher) -> None:
    """Registers user message handlers to dispatcher"""
    dispatcher.message.register(user_start_handler, Command(commands=["start", "help"]))
    dispatcher.message.register(
        add_joke_handler, Text(text=str(Buttons.ADD_JOKE.value))
    )
    dispatcher.message.register(
        watch_jokes_handler, Text(text=Buttons.WATCH_JOKES.value)
    )
    dispatcher.message.register(joke_was_introduced, AddingJoke.inputting_joke_text)
