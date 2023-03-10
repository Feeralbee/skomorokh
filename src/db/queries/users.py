"""Queries to users table"""
from datetime import datetime
from src.db.connector import Connector


def add_user(connector: Connector, user_id: int, user_name: str):
    """Adds user to the users table"""
    cursor = connector.get_cursor()
    query = """INSERT INTO users (
                 user_telegram_id, telegram_nickname,
                 registration_date
               )
               VALUES
                 (%s, %s, %s) ON CONFLICT (user_telegram_id) DO
               UPDATE
               SET
                 telegram_nickname = %s"""
    cursor.execute(query, (user_id, user_name, datetime.now(), user_name))
    connector.connection.commit()
