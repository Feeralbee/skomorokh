"""Utils"""
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from src.keyboards import inline
from src.db.queries.jokes import get_under_consideration_joke, update_publication_status
from src.keyboards import reply
from src.db.connector import Connector
from src.misc.status import Status
from src.handlers.states import ManagingNewJokes


async def manage_jokes(
    message: Message, state: FSMContext, dbconnector: Connector
) -> None:
    """Manages jokes"""
    data = get_under_consideration_joke(dbconnector)
    if data is None:
        await message.answer(
            "Новых анекдотов не найдено", reply_markup=reply.main_menu_keyboard()
        )
        await state.clear()
    else:
        joke_id, joke_text = data
        await message.answer(
            joke_text, reply_markup=inline.get_managing_new_jokes_keyboard()
        )
        await state.set_state(ManagingNewJokes.choosing_an_action)
        await state.update_data(joke_id=joke_id)


async def set_publication_status(
    call: CallbackQuery,
    state: FSMContext,
    dbconnector: Connector,
    publication_status: Status,
) -> None:
    """Sets publication status"""
    data = await state.get_data()
    update_publication_status(dbconnector, data["joke_id"], publication_status)
    await call.message.edit_reply_markup(reply_markup=None)
