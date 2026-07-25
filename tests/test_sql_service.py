from pathlib import Path

import pytest

from models.sql_models import SQLRequest
from services.sql.sql_service import SQLService


DATABASE_PATH = Path("data/healthcare.db")


@pytest.fixture
def sql_service() -> SQLService:
    """
    Create a SQLService instance for testing.
    """
    return SQLService(DATABASE_PATH)


def test_execute_valid_query(sql_service: SQLService):
    """
    Test that a valid SELECT query executes successfully.
    """

    request = SQLRequest(
        query="SELECT * FROM patients LIMIT 5"
    )

    response = sql_service.execute(request)

    assert response.query == request.query
    assert response.row_count == 5
    assert len(response.columns) > 0
    assert len(response.rows) == 5
    assert response.execution_time_ms > 0


def test_reject_empty_query(sql_service: SQLService):
    """
    Test that an empty query raises ValueError.
    """

    request = SQLRequest(
        query=""
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)


def test_reject_drop_table(sql_service: SQLService):
    """
    Test that DROP TABLE is rejected.
    """

    request = SQLRequest(
        query="DROP TABLE patients"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)


def test_reject_delete_query(sql_service: SQLService):
    """
    Test that DELETE is rejected.
    """

    request = SQLRequest(
        query="DELETE FROM patients"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)


def test_reject_update_query(sql_service: SQLService):
    """
    Test that UPDATE is rejected.
    """

    request = SQLRequest(
        query="UPDATE patients SET FIRST='John'"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)
        
        
def test_reject_multiple_statements(sql_service):
    request = SQLRequest(
        query="SELECT * FROM patients; DROP TABLE patients;"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)


def test_reject_sql_comment(sql_service):
    request = SQLRequest(
        query="SELECT * FROM patients -- comment"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)


def test_reject_multiline_comment(sql_service):
    request = SQLRequest(
        query="SELECT * FROM patients /* comment */"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)
        
        
def test_reject_unknown_table(sql_service):

    request = SQLRequest(
        query="SELECT * FROM xyz_table"
    )

    with pytest.raises(ValueError):
        sql_service.execute(request)
        

def test_get_schema(sql_service: SQLService):

    schema = sql_service.database_manager.get_schema()

    assert isinstance(schema, str)
    assert "Table:" in schema
    assert "patients" in schema.lower()