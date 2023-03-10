"""Update filter class IsAdmin"""
from typing import Union, Dict, Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
from src.db.queries.users import checks_user_is_admin
from src.db.connector import Connector


class IsAdmin(BaseFilter):
    """Checks whether the user is an admin"""

    async def __call__(
        self, message: Message, dbconnector: Connector
    ) -> Union[bool, Dict[str, Any]]:
        result: bool = checks_user_is_admin(dbconnector, message.from_user.id)
        return result
