from dataclasses import dataclass


@dataclass
class RetrievalTestCase:
    """
    One retrieval benchmark example.
    """

    question: str

    expected_source: str

    expected_chunks: list[int]

    description: str = ""