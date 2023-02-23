"""Initialize bot and run events dispathcing"""
import logging
from aiogram import Bot, Dispatcher
from src.config import load_config
from src.handlers.user import register_user_handlers

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """
    Initialize Bot instance with an default parse mode which will be passed to all API calls
    And the run events dispatching
    """
    config = load_config(".env")
    bot = Bot(str(config.bot_token), parse_mode="HTML")
    dispatcher = Dispatcher()
    register_user_handlers(dispatcher)
    dispatcher.run_polling(bot)


if __name__ == "__main__":
    main()
