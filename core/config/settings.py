from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    MODEL_NAME: str = "gemini-2.5-flash"
    EMBEDDING_MODEL: str
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    EXCELLENT_DISTANCE_THRESHOLD: float = 0.20
    GOOD_DISTANCE_THRESHOLD: float = 0.35
    AVERAGE_DISTANCE_THRESHOLD: float = 0.50
    OPIK_PROJECT_NAME: str = "ClaimSense-AI"
    VECTOR_WEIGHT: float = 0.8
    BM25_WEIGHT: float = 0.2
    RRF_CONSTANT: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()