from google import genai
from core.config.settings import settings
import opik

class EmbeddingService:
    def __init__(self):
        self.client = genai.Client(
            api_key = settings.GOOGLE_API_KEY
        )
        
    @opik.track(
        type = "tool"
    )
    def generate_embedding(self, text: str) -> list[float]:
        response = self.client.models.embed_content(
            model = settings.EMBEDDING_MODEL,
            contents = text
        )
        return response.embeddings[0].values
    
    
    def generate_embeddings( self, texts: list[str] ) -> list[list[float]]:


        embeddings = []

        total = len(texts)

        print(f"\nGenerating embeddings for {total} chunks...\n")

        for index, text in enumerate(texts, start=1):

            print(f"Embedding {index}/{total}")

            embedding = self.generate_embedding(text)

            embeddings.append(embedding)

        return embeddings