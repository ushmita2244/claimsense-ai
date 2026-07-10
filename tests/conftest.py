import pytest

from services.evaluation.diagnostics_service import DiagnosticsService
from services.attribution.attribution_service import AttributionService


@pytest.fixture
def diagnostics_service():
    return DiagnosticsService()


@pytest.fixture
def attribution_service():
    return AttributionService()