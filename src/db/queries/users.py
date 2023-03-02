"""Queries to users table"""
from datetime import datetime
from src.db.connector import Connector


def add_user(connector: Connector, user_id: int, user_name: str):
    """Adds user to the users table"""
    cursor = connector.get_cursor()
    query = """INSERT INTO users (id, nickname, created_at)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET nickname= %s"""
    cursor.execute(query, (user_id, user_name, datetime.now(), user_name))
    connector.connection.commit()
