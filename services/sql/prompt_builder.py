from textwrap import dedent


class SQLPromptBuilder:
    """
    Builds prompts for SQL generation.
    """

    @staticmethod
    def build_generation_prompt(
        question: str,
        schema: str,
    ) -> str:
        """
        Build the prompt used to generate a SQL query.

        Args:
            question: User's natural language question.
            schema: Database schema.

        Returns:
            Prompt for SQL generation.
        """

        return dedent(
            f"""
            You are an expert SQLite assistant.

            Your task is to convert the user's question into a valid SQLite query.

            Database Schema:
            {schema}

            Rules:
            - Generate ONLY a SQL query.
            - Do NOT include markdown.
            - Do NOT include explanations.
            - Use only the tables and columns provided in the schema.
            - Generate a single SELECT statement.
            - Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or other modifying queries.
            - If the question cannot be answered using the schema, return:
            INVALID_QUERY

            User Question:
            {question}
            """
        ).strip()