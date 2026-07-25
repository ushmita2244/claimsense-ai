from pathlib import Path

import pytest

from models.sql_models import (
    SQLGenerationResponse,
    SQLResponse,
)
from services.sql.sql_response_formatter import SQLResponseFormatter
from services.tools.sql_tool import SQLTool


DATABASE_PATH = Path("data/healthcare.db")


@pytest.fixture
def sql_tool() -> SQLTool:
    return SQLTool(DATABASE_PATH)


def test_execute_success(
    sql_tool,
    monkeypatch,
):
    """
    Test successful SQL tool execution.
    """

    def mock_generate_sql(request):
        return SQLGenerationResponse(
            sql_query="SELECT * FROM patients;"
        )

    def mock_execute(request):
        return SQLResponse(
            query=request.query,
            columns=["FIRST", "LAST"],
            rows=[
                ["John", "Smith"],
                ["Mary", "Johnson"],
            ],
            row_count=2,
            execution_time_ms=5.2,
        )

    def mock_formatter(response):
        return "Formatted SQL Result"

    monkeypatch.setattr(
        sql_tool.sql_service,
        "generate_sql",
        mock_generate_sql,
    )

    monkeypatch.setattr(
        sql_tool.sql_service,
        "execute",
        mock_execute,
    )

    monkeypatch.setattr(
        SQLResponseFormatter,
        "format",
        mock_formatter,
    )

    result = sql_tool.execute(
        question="Show all patients."
    )

    assert result.output == "Formatted SQL Result"

    assert result.metadata == {
        "sql_query": "SELECT * FROM patients;",
        "row_count": 2,
        "execution_time_ms": 5.2,
    }


def test_execute_missing_question(sql_tool):
    """
    Test missing question argument.
    """

    with pytest.raises(ValueError):
        sql_tool.execute()


def test_generate_sql_failure(
    sql_tool,
    monkeypatch,
):
    """
    Test SQL generation failure.
    """

    def mock_generate_sql(request):
        raise ValueError("Generation failed.")

    monkeypatch.setattr(
        sql_tool.sql_service,
        "generate_sql",
        mock_generate_sql,
    )

    with pytest.raises(ValueError):
        sql_tool.execute(
            question="Show patients."
        )


def test_execute_sql_failure(
    sql_tool,
    monkeypatch,
):
    """
    Test SQL execution failure.
    """

    def mock_generate_sql(request):
        return SQLGenerationResponse(
            sql_query="SELECT * FROM patients;"
        )

    def mock_execute(request):
        raise ValueError("Execution failed.")

    monkeypatch.setattr(
        sql_tool.sql_service,
        "generate_sql",
        mock_generate_sql,
    )

    monkeypatch.setattr(
        sql_tool.sql_service,
        "execute",
        mock_execute,
    )

    with pytest.raises(ValueError):
        sql_tool.execute(
            question="Show patients."
        )