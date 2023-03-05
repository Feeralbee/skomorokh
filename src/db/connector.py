"""Class Connector"""
import psycopg


class Connector:
    """Connecting to database"""

    def __init__(self, connection_str: str):
        self.connection = psycopg.connect(connection_str)

    def get_cursor(self):
        """Get cursor"""
        return self.connection.cursor()

    def __del__(self):
        self.connection.close()
