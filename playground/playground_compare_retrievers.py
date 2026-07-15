from datasets.retrieval_dataset import RETRIEVAL_DATASET

from services.retrieval.retriever import Retriever
from services.retrieval.hybrid_retriever import HybridRetriever
from services.evaluation.retrieval_benchmark import RetrievalBenchmark


def print_report(title, report):

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    print(f"Total Queries        : {report.total_queries}")
    print(f"Successful Retrievals: {report.successful_retrievals}")
    print(f"Success Rate         : {report.success_rate:.2%}")
    print(f"Average Precision@3 : {report.average_precision:.3f}")
    print(f"Average Recall@3    : {report.average_recall:.3f}")
    print(f"Mean Reciprocal Rank: {report.mean_reciprocal_rank:.3f}")


def main():

    vector_report = RetrievalBenchmark(
        retriever=Retriever(),
        dataset=RETRIEVAL_DATASET
    ).run(top_k=3)

    hybrid_report = RetrievalBenchmark(
        retriever=HybridRetriever(),
        dataset=RETRIEVAL_DATASET
    ).run(top_k=3)

    print_report(
        "VECTOR RETRIEVAL",
        vector_report
    )

    print_report(
        "HYBRID RETRIEVAL",
        hybrid_report
    )

    print("\n" + "=" * 80)
    print("IMPROVEMENT")
    print("=" * 80)

    print(
        f"Success Rate : "
        f"{vector_report.success_rate:.2%} "
        f"→ "
        f"{hybrid_report.success_rate:.2%}"
    )

    print(
        f"Precision@3 : "
        f"{vector_report.average_precision:.3f} "
        f"→ "
        f"{hybrid_report.average_precision:.3f}"
    )

    print(
        f"Recall@3 : "
        f"{vector_report.average_recall:.3f} "
        f"→ "
        f"{hybrid_report.average_recall:.3f}"
    )

    print(
        f"MRR : "
        f"{vector_report.mean_reciprocal_rank:.3f} "
        f"→ "
        f"{hybrid_report.mean_reciprocal_rank:.3f}"
    )


if __name__ == "__main__":
    main()