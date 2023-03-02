"""MiddlewareConnector class"""
from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from src.db.connector import Connector


class DBConnector(BaseMiddleware):  # pylint: disable=R0903
    """Middleware to get database connector in handler"""

    def __init__(self, connection_str: str) -> None:
        self.connection_string = connection_str

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        data["dbconnector"] = Connector(self.connection_string)
        return await handler(event, data)
