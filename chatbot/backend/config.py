from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    # API Keys
    cohere_api_key: str
    gemini_api_key: str

    # Qdrant Configuration
    qdrant_url: str
    qdrant_api_key: str

    # Database Configuration
    neon_database_url: str

    # Security
    secret_key: str
    allowed_origins: List[str]

    # RAG Configuration
    max_question_length: int = 2000
    max_selected_text_length: int = 5000
    max_sources_per_response: int = 5
    top_k_chunks: int = 5  # Increased to 5 chunks for better context

    # Rate Limiting
    rate_limit_requests: int = 10
    rate_limit_window: int = 60  # seconds

    # Embedding Model
    embedding_model: str = "embed-english-v3.0"

    # LLM Configuration
    llm_model: str = "gemini-2.5-flash"
    max_tokens: int = 500
    temperature: float = 0.7

    class Config:
        env_file = ".env"
        case_sensitive = False


# Create a singleton instance
settings = Settings()