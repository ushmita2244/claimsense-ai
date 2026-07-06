from services.embeddings.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

embedding = embedding_service.generate_embedding(
    "Health insurance covers surgery."
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])