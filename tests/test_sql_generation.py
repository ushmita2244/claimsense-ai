from pathlib import Path

import pytest

from models.sql_models import SQLGenerationRequest
from services.sql.sql_service import SQLService


DATABASE_PATH = Path("data/healthcare.db")


@pytest.fixture
def sql_service() -> SQLService:
    return SQLService(DATABASE_PATH)


def test_generate_sql_success(sql_service, monkeypatch):
    """
    Test successful SQL generation.
    """

    def mock_generate_response(prompt: str) -> str:
        return "SELECT * FROM patients;"

    monkeypatch.setattr(
        sql_service.llm,
        "generate_response",
        mock_generate_response,
    )

    response = sql_service.generate_sql(
        SQLGenerationRequest(
            question="Show all patients."
        )
    )

    assert response.sql_query == "SELECT * FROM patients;"
    

def test_generate_sql_markdown(sql_service, monkeypatch):

    def mock_generate_response(prompt: str) -> str:
        return """```sql
SELECT * FROM patients;
```"""

    monkeypatch.setattr(
        sql_service.llm,
        "generate_response",
        mock_generate_response,
    )

    response = sql_service.generate_sql(
        SQLGenerationRequest(
            question="Show all patients."
        )
    )

    assert response.sql_query == "SELECT * FROM patients;"
    
    
def test_generate_sql_unknown_table(sql_service, monkeypatch):

    def mock_generate_response(prompt: str) -> str:
        return "SELECT * FROM unknown_table;"

    monkeypatch.setattr(
        sql_service.llm,
        "generate_response",
        mock_generate_response,
    )

    with pytest.raises(ValueError):
        sql_service.generate_sql(
            SQLGenerationRequest(
                question="Show everything."
            )
        )
        

def test_generate_sql_drop_table(sql_service, monkeypatch):

    def mock_generate_response(prompt: str) -> str:
        return "DROP TABLE patients;"

    monkeypatch.setattr(
        sql_service.llm,
        "generate_response",
        mock_generate_response,
    )

    with pytest.raises(ValueError):
        sql_service.generate_sql(
            SQLGenerationRequest(
                question="Delete table."
            )
        )
        
        
def test_generate_sql_empty_response(sql_service, monkeypatch):

    def mock_generate_response(prompt: str) -> str:
        return ""

    monkeypatch.setattr(
        sql_service.llm,
        "generate_response",
        mock_generate_response,
    )

    with pytest.raises(ValueError):
        sql_service.generate_sql(
            SQLGenerationRequest(
                question="Show all patients."
            )
        )