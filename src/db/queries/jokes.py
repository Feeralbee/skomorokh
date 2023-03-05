"""Queries to jokes table"""
from datetime import datetime
from src.db.connector import Connector


def add_joke(connector: Connector, joke: str, user_id: int):
    """Add joke in jokes table"""
    cursor = connector.get_cursor()
    query = """INSERT INTO jokes (joke, author_id, created_at)
               VALUES
                 (%s, %s, %s)"""
    cursor.execute(query, (joke, user_id, datetime.now()))
    connector.connection.commit()
