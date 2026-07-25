from models.sql_models import SQLResponse


class SQLResponseFormatter:
    """
    Formats SQL query results into a human-readable representation
    suitable for LLM consumption.
    """

    DEFAULT_MAX_ROWS = 20

    @classmethod
    def format(
        cls,
        response: SQLResponse,
        max_rows: int = DEFAULT_MAX_ROWS,
    ) -> str:
        """
        Format a SQLResponse into text.

        Args:
            response: SQL execution result.
            max_rows: Maximum number of rows to include.

        Returns:
            Formatted string.
        """

        sections: list[str] = []

        # SQL Query
        sections.append("Executed SQL:")
        sections.append(response.query)
        sections.append("")

        # Columns
        sections.append("Columns:")

        if response.columns:
            sections.append(", ".join(response.columns))
        else:
            sections.append("None")

        sections.append("")

        # Rows
        sections.append("Rows:")

        if response.rows:

            displayed_rows = response.rows[:max_rows]

            for index, row in enumerate(displayed_rows, start=1):

                sections.append(f"Row {index}")

                for column, value in zip(response.columns, row):
                    display_value = "NULL" if value is None else str(value)
                    sections.append(f"{column}: {display_value}")

                sections.append("")

            omitted_rows = response.row_count - len(displayed_rows)

            if omitted_rows > 0:
                sections.append(
                    f"... {omitted_rows} additional row(s) omitted."
                )
                sections.append("")

        else:
            sections.append("No rows returned.")
            sections.append("")

        sections.append(
            f"Returned {response.row_count} row(s)."
        )

        return "\n".join(sections)