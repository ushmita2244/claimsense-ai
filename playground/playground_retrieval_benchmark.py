from datasets.retrieval_dataset import RETRIEVAL_DATASET

from services.retrieval.retriever import Retriever
from services.evaluation.retrieval_benchmark import RetrievalBenchmark


def print_separator():

    print("=" * 80)


def main():

    benchmark = RetrievalBenchmark(
        retriever=Retriever(),
        dataset=RETRIEVAL_DATASET
    )

    report = benchmark.run(top_k=3)

    print_separator()
    print("RETRIEVAL BENCHMARK")
    print_separator()

    print(f"Total Queries        : {report.total_queries}")
    print(f"Successful Retrievals: {report.successful_retrievals}")
    print(f"Success Rate         : {report.success_rate:.2%}")
    print(f"Average Precision@3 : {report.average_precision:.3f}")
    print(f"Average Recall@3    : {report.average_recall:.3f}")
    print(f"Mean Reciprocal Rank: {report.mean_reciprocal_rank:.3f}")

    print_separator()
    print("DETAILED RESULTS")
    print_separator()

    for index, result in enumerate(report.results, start=1):

        print(f"\nTest Case {index}")
        print("-" * 80)

        print(f"Question          : {result.test_case.question}")
        print(f"Description       : {result.test_case.description}")
        print(f"Expected Source   : {result.test_case.expected_source}")
        print(f"Expected Chunks   : {result.test_case.expected_chunks}")

        print(f"\nDocument Match    : {result.document_match}")
        print(f"Chunk Match       : {result.chunk_match}")
        print(f"Precision@3       : {result.precision_at_k:.3f}")
        print(f"Recall@3          : {result.recall_at_k:.3f}")
        print(f"MRR               : {result.reciprocal_rank:.3f}")

        print("\nRetrieved Documents")

        for rank, document in enumerate(result.retrieved_documents, start=1):

            print(
                f"{rank}. "
                f"{document.source} | "
                f"Chunk {document.chunk_number} | "
                f"Distance {document.distance:.4f}"
            )


if __name__ == "__main__":
    main()