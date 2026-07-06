from google import genai
from core.config.settings import settings
import numpy as np

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

sentences = [
    "Health insurance covers surgery.",
    "Medical insurance pays for operations.",
    "The Sun is the largest star in our solar system."
]


# Generate embeddings for each sentence

embeddings = []

for sentence in sentences:
    response = client.models.embed_content(
        model = settings.EMBEDDING_MODEL,
        contents = sentence
    )
    embedding = response.embeddings[0].values

    embeddings.append(embedding)
    
    
#  Cosine Similarity Function
def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot_product = np.dot(vec1, vec2)

    magnitude1 = np.linalg.norm(vec1)

    magnitude2 = np.linalg.norm(vec2)

    return dot_product / (magnitude1 * magnitude2)


# Calculate similarities

print("=" * 80)

print("Sentence A ↔ Sentence B")

print(
    cosine_similarity(
        embeddings[0],
        embeddings[1]
    )
)

print("=" * 80)

print("Sentence A ↔ Sentence C")

print(
    cosine_similarity(
        embeddings[0],
        embeddings[2]
    )
)

