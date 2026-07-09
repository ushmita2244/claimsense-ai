import pytest

from services.evaluation.diagnostics_service import DiagnosticsService

@pytest.fixture
def diagnostics_service():
    """
    Returns a fresh DiagnosticsService instance
    for every test.
    """

    return DiagnosticsService()