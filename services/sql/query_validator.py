import re


class QueryValidator:
    """
    Validates SQL queries before execution.
    Only read-only SELECT statements are allowed.
    """

    FORBIDDEN_KEYWORDS = {
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "replace",
        "attach",
        "detach",
        "pragma",
        "vacuum",
        "reindex",
    }

    @classmethod
    def validate(
        cls,
        query: str,
        available_tables: set[str],
    ) -> None:
        """
        Validate a SQL query.

        Args:
            query: SQL query.
            allowed_tables: Tables available in the database.

        Raises:
            ValueError: If the query is unsafe.
        """

        if not query or not query.strip():
            raise ValueError("SQL query cannot be empty.")

        normalized_query = query.strip().lower()

        # -----------------------------------------
        # Only SELECT queries
        # -----------------------------------------

        if not normalized_query.startswith("select"):
            raise ValueError("Only SELECT queries are allowed.")

        # -----------------------------------------
        # Reject multiple statements
        # -----------------------------------------

        query_without_trailing_semicolon = normalized_query.rstrip(";")

        if ";" in query_without_trailing_semicolon:
            raise ValueError("Multiple SQL statements are not allowed.")

        # -----------------------------------------
        # Reject SQL comments
        # -----------------------------------------

        if "--" in normalized_query:
            raise ValueError("SQL comments are not allowed.")

        if "/*" in normalized_query or "*/" in normalized_query:
            raise ValueError("SQL comments are not allowed.")

        # -----------------------------------------
        # Reject dangerous keywords
        # -----------------------------------------

        for keyword in cls.FORBIDDEN_KEYWORDS:

            if re.search(rf"\b{keyword}\b", normalized_query):
                raise ValueError(
                    f"Forbidden SQL keyword detected: {keyword.upper()}"
                )

        # -----------------------------------------
        # Validate table names
        # -----------------------------------------

        referenced_tables = re.findall(
            r"(?:from|join)\s+([a-zA-Z_]\w*)",
            normalized_query,
            flags=re.ASCII,
        )

        for table in referenced_tables:

            if table not in available_tables:
                raise ValueError(
                    f"Unknown table referenced: {table}"
                )