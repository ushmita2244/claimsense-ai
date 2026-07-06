from services.retrieval.retriever import Retriever

retriever = Retriever()

query = "Does insurance cover hospitalization?"

results = retriever.retrieve(query)

print("=" * 80)
print("RETRIEVED DOCUMENTS")
print("=" * 80)

for doc in results["documents"][0]:
    print(doc)
    print("-" * 80)