"""Tests for src/db/queries/jokes.py"""
from unittest.mock import MagicMock
from src.db.connector import Connector
from src.misc.status import Status
from src.db.queries.jokes import get_under_consideration_joke


def test_get_under_consideration_joke():
    """Test get_under_consideration_joke function"""
    connector_mock = MagicMock(spec=Connector)
    cursor_mock = MagicMock(name="cursor_mock")
    connector_mock.get_cursor.return_value = cursor_mock

    expected_result = (1, "Test joke")
    cursor_mock.fetchone.return_value = expected_result

    result = get_under_consideration_joke(connector_mock)

    connector_mock.get_cursor.assert_called_once()
    cursor_mock.execute.assert_called_once_with(
        """SELECT
                joke_id,
                joke_text
               FROM
                jokes
               WHERE
                publication_status = %s
               ORDER BY
                joke_id
               LIMIT
                1""",
        (Status.UNDER_CONSIDERATION.value,),
    )
    assert result == expected_result
