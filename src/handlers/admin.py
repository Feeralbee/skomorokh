"""Processing messages from users"""
from aiogram import Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from src.keyboards.reply import main_menu_keyboard
from src.handlers.states import ManagingNewJokes
from src.db.connector import Connector
from src.filters.is_admin import IsAdmin
from src.misc import utils


async def command_managing_new_jokes_handler(
    message: Message, state: FSMContext, dbconnector: Connector
) -> None:
    """This procedure handles '/managing_new_jokes' command"""
    await message.answer("Режим проверки анекдотов", reply_markup=ReplyKeyboardRemove)
    await utils.manage_jokes(message, state, dbconnector)


async def approve_anecdote_handler(
    call: CallbackQuery, state: FSMContext, dbconnector: Connector
) -> None:
    """This procedure handles 'approve' callback data"""
    await utils.set_publication_status(call, state, dbconnector, "approved")
    await utils.manage_jokes(call.message, state, dbconnector)


async def disapprove_anecdote_handler(
    call: CallbackQuery, state: FSMContext, dbconnector: Connector
) -> None:
    """This procedure handles 'disapprove' callback data"""
    await utils.set_publication_status(call, state, dbconnector, "not_approved")
    await utils.manage_jokes(call.message, state, dbconnector)


async def command_stop_managing_handler(message: Message, state: FSMContext) -> None:
    """This procedure handles '/stop_managing' command"""
    await state.clear()
    await message.answer(
        "Выход из режима проверки анекдотов", reply_markup=main_menu_keyboard()
    )


def register_admin_handlers(dispatcher: Dispatcher) -> None:
    """Registers admin message handlers to dispatcher"""
    dispatcher.message.register(
        command_managing_new_jokes_handler,
        Command(commands=["managing_new_jokes"]),
        IsAdmin(),
    )
    dispatcher.callback_query.register(
        approve_anecdote_handler,
        F.data == "approve",
        ManagingNewJokes.choosing_an_action,
        IsAdmin(),
    )
    dispatcher.callback_query.register(
        disapprove_anecdote_handler,
        F.data == "disapprove",
        ManagingNewJokes.choosing_an_action,
        IsAdmin(),
    )
    dispatcher.message.register(
        command_stop_managing_handler,
        Command(commands=["stop_managing"]),
        IsAdmin(),
        ManagingNewJokes.choosing_an_action,
    )
