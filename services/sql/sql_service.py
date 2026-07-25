from pathlib import Path

from core.utils.timer import Timer
from models.sql_models import SQLRequest, SQLResponse
from services.sql.database_manager import DatabaseManager
from services.sql.query_validator import QueryValidator
from services.llm.gemini_service import GeminiService
from services.sql.prompt_builder import SQLPromptBuilder
from models.sql_models import (
    SQLGenerationRequest,
    SQLGenerationResponse,
)
from services.parser.sql_parser import SQLParser


class SQLService:
    """
    Service responsible for executing validated SQL queries.
    """

    def __init__(self, database_path: str | Path):

        self.database_manager = DatabaseManager(database_path)
        self.llm = GeminiService()

    def execute(
        self,
        request: SQLRequest
    ) -> SQLResponse:
        """
        Validate and execute a SQL query.

        Args:
            request: SQL execution request.

        Returns:
            SQLResponse containing query results.
        """
        
        available_tables = self.database_manager.get_tables()
        # ==========================================
        # Validate Query
        # ==========================================

        QueryValidator.validate(
            request.query,
            available_tables=available_tables,
        )

        # ==========================================
        # Execute Query
        # ==========================================

        with Timer() as timer:

            response = self.database_manager.execute_query(
                request.query
            )

        # ==========================================
        # Performance Metrics
        # ==========================================

        response.execution_time_ms = timer.elapsed

        return response
    
    
    def generate_sql(
        self,
        request: SQLGenerationRequest,
    ) -> SQLGenerationResponse:
        """
        Generate a SQL query from a natural language question.

        Args:
            request: SQL generation request.

        Returns:
            SQLGenerationResponse containing the validated SQL query.
        """

        # ==========================================
        # Retrieve Database Schema
        # ==========================================

        schema = self.database_manager.get_schema()
        
        available_tables = self.database_manager.get_tables()

        # ==========================================
        # Build Prompt
        # ==========================================

        prompt = SQLPromptBuilder.build_generation_prompt(
            question=request.question,
            schema=schema,
        )

        # ==========================================
        # Generate SQL
        # ==========================================

        llm_response = self.llm.generate_response(
            prompt
        )

        # ==========================================
        # Parse SQL
        # ==========================================

        sql_response = SQLParser.parse(
            llm_response
        )
        
        # ==========================================
        # Validate SQL
        # ==========================================
        
        QueryValidator.validate(
            query=sql_response.sql_query,
            available_tables=available_tables,
        )

        # ==========================================
        # Return SQL
        # ==========================================

        return sql_response