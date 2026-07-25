import sqlite3
from pathlib import Path
from models.sql_models import SQLResponse


class DatabaseManager:
    """
    Handles all interactions with the SQLite database.
    """

    def __init__(self, database_path: str | Path):
        self.database_path = str(database_path)

    def execute_query(self, query: str) -> SQLResponse:
        """
        Execute a read-only SQL query.

        Args:
            query: SQL SELECT query.

        Returns:
            Tuple containing:
            - List of column names
            - List of result rows
        """

        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()

            cursor.execute(query)

            rows = cursor.fetchall()

            columns = (
                [column[0] for column in cursor.description]
                if cursor.description
                else []
            )

            return SQLResponse(
                query=query,
                columns=columns,
                rows=[list(row) for row in rows],
                row_count=len(rows)
            )

        finally:
            connection.close()
            
            
    def get_tables(self) -> set[str]:
        """
        Return all user-defined tables in the database.
        """

        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table'
            """)

            return {
                row[0].lower()
                for row in cursor.fetchall()
            }

        finally:
            connection.close()
            
    
    def get_schema(self) -> str:
        """
        Return the database schema as formatted text.
        """

        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                ORDER BY name
            """)

            tables = [row[0] for row in cursor.fetchall()]

            schema = []

            for table in tables:

                cursor.execute(f"PRAGMA table_info({table})")

                columns = cursor.fetchall()

                schema.append(f"Table: {table}")

                for column in columns:

                    schema.append(
                        f"  - {column[1]} ({column[2]})"
                    )

                schema.append("")

            return "\n".join(schema)

        finally:
            connection.close()