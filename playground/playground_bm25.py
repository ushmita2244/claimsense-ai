from services.retrieval.bm25_service import BM25Service


def main():

    bm25 = BM25Service()

    while True:

        print("\n" + "=" * 80)

        query = input("Question: ")

        if query.lower() == "exit":
            break

        documents = bm25.search(
            query=query,
            top_k=3
        )

        print("\nTop Results\n")

        for index, document in enumerate(documents, start=1):

            print(f"Rank {index}")
            print(f"Source : {document.source}")
            print(f"Chunk  : {document.chunk_number}")
            print("-" * 60)
            print(document.text[:350])
            print()
            

if __name__ == "__main__":
    main()