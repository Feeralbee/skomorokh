"""Class Config"""
from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    """Containing config data"""

    bot_token: str
    admin_ids: list[int]


def load_config(path: str = "") -> Config:
    """Return object of Config initiliaze this from .env file"""
    env = Env()
    env.read_env(path)

    return Config(bot_token=env.str("BOT_TOKEN"), admin_ids=env.list("ADMINS"))
