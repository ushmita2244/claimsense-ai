from langchain_google_genai import ChatGoogleGenerativeAI

from core.config.settings import settings

from services.llm.base_llm import BaseLLM
import opik

class GeminiService(BaseLLM):
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0
        )

    @opik.track(
        type = "llm"
    )
    def generate_response(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content