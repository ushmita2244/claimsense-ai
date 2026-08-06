from pathlib import Path

from models.sql_models import (
    SQLGenerationRequest,
    SQLRequest,
)
from models.tool_definition import ToolDefinition
from models.tool_parameter import ToolParameter
from models.tool_result import ToolResult
from services.sql.sql_response_formatter import SQLResponseFormatter
from services.sql.sql_service import SQLService
from services.tools.base_tool import BaseTool
from models.knowledge_source import KnowledgeSource


class SQLTool(BaseTool):
    """
    Tool for answering structured healthcare questions
    using the SQL database.
    """

    def __init__(
        self,
        database_path: str | Path,
    ) -> None:
        """
        Initialize the SQL tool.

        Args:
            database_path: Path to the SQLite database.
        """

        self.sql_service = SQLService(database_path)

    @property
    def definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="sql_tool",
            description=(
                "Answers questions by generating and executing SQL "
                "queries against the structured healthcare database."
            ),
            parameters=[
                ToolParameter(
                    name="question",
                    description="The user's question.",
                    type="string",
                    required=True,
                )
            ],
        )
    
    def execute(
        self,
        **kwargs,
    ) -> ToolResult:
        """
        Execute the SQL tool.

        Args:
            **kwargs: Tool arguments.

        Returns:
            Standardized tool result.
        """

        question = self._get_question(kwargs)

        # Generate SQL
        sql_generation_response = self.sql_service.generate_sql(
            SQLGenerationRequest(
                question=question,
            )
        )

        # Execute SQL
        sql_response = self.sql_service.execute(
            SQLRequest(
                query=sql_generation_response.sql_query,
            )
        )

        # Format for LLM
        formatted_response = SQLResponseFormatter.format(
            sql_response
        )

        return ToolResult(
            output=formatted_response,
            metadata={
                "sql_query": sql_response.query,
                "row_count": sql_response.row_count,
                "execution_time_ms": sql_response.execution_time_ms,
            },
            knowledge_sources=[
                KnowledgeSource.SQL_DATABASE,
            ],
        )


    @staticmethod
    def _get_question(
        kwargs: dict,
    ) -> str:
        """
        Extract the user's question from the tool arguments.

        Args:
            kwargs: Tool arguments.

        Returns:
            User question.

        Raises:
            ValueError: If the question is missing.
        """

        question = kwargs.get("question")

        if not question:
            raise ValueError(
                "SQLTool requires a 'question' argument."
            )

        return question