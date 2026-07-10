from tests.helpers import make_document
from models.source_attribution import SourceAttribution

from tests.helpers import make_chunk


def test_groups_documents_by_source(attribution_service):

    documents = [

        make_document(
            source="WHO.pdf",
            chunk_number=2,
            distance=0.20
        ),

        make_document(
            source="WHO.pdf",
            chunk_number=7,
            distance=0.18
        ),

        make_document(
            source="Cancer.pdf",
            chunk_number=3,
            distance=0.25
        )

    ]

    citations = attribution_service.build(documents)

    assert len(citations) == 2
    

def test_chunks_are_sorted_by_distance(attribution_service):

    documents = [

        make_document(
            source="WHO.pdf",
            chunk_number=8,
            distance=0.30
        ),

        make_document(
            source="WHO.pdf",
            chunk_number=2,
            distance=0.10
        ),

        make_document(
            source="WHO.pdf",
            chunk_number=4,
            distance=0.20
        )

    ]

    citations = attribution_service.build(documents)

    chunks = citations[0].chunks

    assert chunks[0].distance == 0.10
    assert chunks[1].distance == 0.20
    assert chunks[2].distance == 0.30
    

def test_sources_are_sorted_by_best_distance(attribution_service):

    documents = [

        make_document(
            source="Cancer.pdf",
            chunk_number=1,
            distance=0.40
        ),

        make_document(
            source="WHO.pdf",
            chunk_number=1,
            distance=0.12
        )

    ]

    citations = attribution_service.build(documents)

    assert citations[0].source == "WHO.pdf"
    assert citations[1].source == "Cancer.pdf"
    
    
def test_best_distance_property():

    citation = SourceAttribution(

        source="WHO.pdf",

        chunks=[

            make_chunk(
                chunk_number=5,
                distance=0.10
            ),

            make_chunk(
                chunk_number=7,
                distance=0.25
            )

        ]

    )

    assert citation.best_distance == 0.10
    

def test_single_source_returns_single_citation(attribution_service):

    documents = [

        make_document(
            source="WHO.pdf",
            chunk_number=1
        )

    ]

    citations = attribution_service.build(documents)

    assert len(citations) == 1

    assert citations[0].source == "WHO.pdf"
    
    
def test_empty_documents_returns_empty_list(attribution_service):

    citations = attribution_service.build([])

    assert citations == []