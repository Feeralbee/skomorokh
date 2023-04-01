"""Queries to jokes table"""
from datetime import datetime
from src.db.connector import Connector
from src.misc.status import Status


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
                publication_status = %s
               ORDER BY
                joke_id
               LIMIT
                1"""
    cursor.execute(query, (Status.UNDER_CONSIDERATION.value,))
    return cursor.fetchone()


def update_publication_status(
    connector: Connector, joke_id: int, publication_status: Status
):
    """Updates publication status for joke by joke_id"""
    cursor = connector.get_cursor()
    query = """UPDATE
                jokes
               SET
                publication_status = %s
               WHERE
                joke_id = %s"""
    cursor.execute(query, (publication_status.value, joke_id))
    connector.connection.commit()
