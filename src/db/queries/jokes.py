"""Queries to jokes table"""
from datetime import datetime
from src.db.connector import Connector


def add_joke(connector: Connector, joke: str, user_id: int):
    """Add joke in jokes table"""
    cursor = connector.get_cursor()
    query = """INSERT INTO jokes (
                 joke_text, author_telegram_id, creation_date
               )
               VALUES
                 (%s, %s, %s)"""
    cursor.execute(query, (joke, user_id, datetime.now()))
    connector.connection.commit()
