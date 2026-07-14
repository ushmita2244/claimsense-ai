from models.retrieval_result import RetrievalResult
from models.retrieval_test_case import RetrievalTestCase
from models.retrieved_document import RetrievedDocument


class RetrievalEvaluator:
    """
    Evaluates retrieval quality for a single benchmark test case.
    """

    def evaluate(
        self,
        test_case: RetrievalTestCase,
        retrieved_documents: list[RetrievedDocument],
        top_k: int
    ) -> RetrievalResult:
        """
        Compare retrieved documents against the expected benchmark answer.
        """
        
        # Convert list to set for O(1) membership checks
        expected_chunks = set(test_case.expected_chunks)

        # ==================================================
        # Document Match
        # ==================================================

        document_match = any(
            document.source == test_case.expected_source
            for document in retrieved_documents
        )

        # ==================================================
        # Chunk Match
        # ==================================================

        chunk_match = any(
            (
                document.source == test_case.expected_source
                and document.chunk_number in expected_chunks
            )
            for document in retrieved_documents
        )

        # ==================================================
        # Count Hits
        # ==================================================

        hits = 0

        for document in retrieved_documents:

            if (
                document.source == test_case.expected_source
                and document.chunk_number in expected_chunks
            ):

                hits += 1

        # ==================================================
        # Precision@K
        # ==================================================

        precision = hits / top_k

        # ==================================================
        # Recall@K
        # ==================================================

        recall = hits / len(expected_chunks)

        # ==================================================
        # Mean Reciprocal Rank (MRR)
        # ==================================================

        reciprocal_rank = 0.0

        for index, document in enumerate(retrieved_documents, start=1):

            if (
                document.source == test_case.expected_source
                and document.chunk_number in expected_chunks
            ):

                reciprocal_rank = 1 / index

                break

        # ==================================================
        # Final Result
        # ==================================================

        return RetrievalResult(
            test_case=test_case,
            retrieved_documents=retrieved_documents,
            document_match=document_match,
            chunk_match=chunk_match,
            precision_at_k=precision,
            recall_at_k=recall,
            reciprocal_rank=reciprocal_rank
        )