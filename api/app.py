from fastapi import FastAPI

from api.models.ask_request import AskRequest
from api.models.ask_response import AskResponse

from src.bootstrap import build_agent
from api.models.health_response import HealthResponse
from api.exceptions.handlers import register_exception_handlers
from core.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Healthcare Conversational RAG",
    contact={
        "name": "Ushmita Marwah",
        "url": "https://github.com/ushmita2244/claimsense-ai",
        "email": "ushmitamarwaha@gmail.com",
    },
)

register_exception_handlers(app)

agent_service = build_agent()


@app.get("/")
def root():

    return {
        "message": "ClaimSense AI API is running."
    }
    
@app.post(
    "/ask",
    response_model=AskResponse
)
def ask(
    request: AskRequest
):

    answer = agent_service.generate_response(
        prompt=request.question,
        session_id=request.session_id
    )

    return AskResponse(
        question=request.question,
        answer=answer
    )
    
    
@app.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return HealthResponse(
        status="healthy",
        version=settings.APP_VERSION
    )