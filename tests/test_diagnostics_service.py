from tests.helpers import make_document
from core.config.settings import settings
import pytest


def test_total_documents(diagnostics_service):
    """
    Diagnostics should count documents correctly.
    """

    documents = [
        make_document(),
        make_document()
    ]

    diagnostics = diagnostics_service.analyze(documents)

    assert diagnostics.total_documents == 2


def test_top_distance(diagnostics_service):
    """
    Should return the minimum distance.
    """

    documents = [
        make_document(distance=0.25),
        make_document(distance=0.15)
    ]

    diagnostics = diagnostics_service.analyze(documents)

    assert diagnostics.top_distance == 0.15


def test_average_distance(diagnostics_service):
    """
    Should calculate average distance.
    """

    documents = [
        make_document(distance=0.20),
        make_document(distance=0.40)
    ]

    diagnostics = diagnostics_service.analyze(documents)

    assert diagnostics.average_distance == pytest.approx(0.30)


def test_unique_sources(diagnostics_service):
    """
    Duplicate sources should be removed.
    """

    documents = [

        make_document(
            source="WHO.pdf"
        ),

        make_document(
            source="WHO.pdf",
            chunk_number=2
        ),

        make_document(
            source="Cancer.pdf",
            chunk_number=3
        )

    ]

    diagnostics = diagnostics_service.analyze(documents)

    assert diagnostics.sources == [
        "Cancer.pdf",
        "WHO.pdf"
    ]


def test_quality_is_excellent(diagnostics_service):
    """
    Small distance should be Excellent.
    """

    documents = [
        make_document(distance=0.10)
    ]

    diagnostics = diagnostics_service.analyze(documents)

    assert diagnostics.retrieval_quality == "Excellent"
    
    
def test_quality_is_good(diagnostics_service):
    
    documents = [
    make_document(
        distance = settings.GOOD_DISTANCE_THRESHOLD - 0.01 )
    ]
    diagnostics = diagnostics_service.analyze(documents)
    assert diagnostics.retrieval_quality == "Good"
    

def test_quality_is_average(diagnostics_service):
    
    documents = [
    make_document(
        distance = settings.AVERAGE_DISTANCE_THRESHOLD - 0.01 )
    ]
    diagnostics = diagnostics_service.analyze(documents)
    assert diagnostics.retrieval_quality == "Average"
    
    
def test_quality_is_poor(diagnostics_service):
    
    documents = [
    make_document(
        distance = settings.AVERAGE_DISTANCE_THRESHOLD + 0.10 )
    ]
    diagnostics = diagnostics_service.analyze(documents)
    assert diagnostics.retrieval_quality == "Poor"
    

