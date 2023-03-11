"""Queries to jokes table"""
from datetime import datetime
from src.db.connector import Connector


def add_joke(connector: Connector, joke: str, user_id: int):
    """Adds joke in jokes table"""
    cursor = connector.get_cursor()
    query = """INSERT INTO jokes (
                 joke_text, author_telegram_id, creation_date
               )
               VALUES
                 (%s, %s, %s)"""
    cursor.execute(query, (joke, user_id, datetime.now()))
    connector.connection.commit()


def get_under_consideration_joke(connector: Connector):
    """Gets the joke_id and joke_text of the joke from the jokes table, which is under review"""
    cursor = connector.get_cursor()
    query = """SELECT
                joke_id,
                joke_text
               FROM
                jokes
               WHERE
                publication_status='under_consideration'
               ORDER BY
                joke_id
               LIMIT
                1"""
    cursor.execute(query)
    return cursor.fetchone()
