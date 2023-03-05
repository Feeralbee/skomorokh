"""Class Config"""
from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    """Containing config data"""

    bot_token: str
    admin_ids: list[int]
    database_connection_str: str


def load_config(path: str = "") -> Config:
    """The returned configuration object initialized from the .env file"""
    env = Env()
    env.read_env(path)

    return Config(
        bot_token=env.str("BOT_TOKEN"),
        admin_ids=env.list("ADMINS"),
        database_connection_str=env.str("DATABASE_CONNECTION_STR"),
    )
