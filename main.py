"""Initialize bot and run events dispatching"""
import logging
import asyncio
from aiogram import Bot, Dispatcher
from src.config import load_config
from src.handlers.user import register_user_handlers
from src.handlers.admin import register_admin_handlers
from src.middlewares.dbconnector import DBConnector

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    """
    Initialize Bot instance with an default parse mode which will be passed to all API calls
    And the run events dispatching
    """
    config = load_config(".env")
    bot = Bot(str(config.bot_token), parse_mode="HTML")
    dispatcher = Dispatcher()
    dispatcher.update.outer_middleware(DBConnector(config.database_connection_str))
    register_admin_handlers(dispatcher)
    register_user_handlers(dispatcher)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
