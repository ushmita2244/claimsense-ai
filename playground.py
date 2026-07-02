from langchain_google_genai import ChatGoogleGenerativeAI
from core.config.settings import settings

llm = ChatGoogleGenerativeAI(
    model=settings.MODEL_NAME,
    google_api_key=settings.GOOGLE_API_KEY,
)

response = llm.invoke("Tell me 3 facts about AI engineering.")

print(response.content)