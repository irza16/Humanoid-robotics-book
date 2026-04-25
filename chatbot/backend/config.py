from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    # API Keys (Optional for basic functionality)
    cohere_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None

    # Qdrant Configuration (Optional for basic functionality)
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None

    # Database Configuration (Optional for basic functionality)
    # Support both NEON_DATABASE_URL and DATABASE_URL (for HF Spaces compatibility)
    neon_database_url: Optional[str] = None

    # Security
    secret_key: str = "dev-secret-key-change-in-production"  # Default for testing
    allowed_origins: List[str] = ["*"]  # Default for testing

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

    def __init__(self, **data):
        super().__init__(**data)
        # For HF Spaces and other platforms, fallback to DATABASE_URL if NEON_DATABASE_URL not set
        if not self.neon_database_url and os.environ.get('DATABASE_URL'):
            self.neon_database_url = os.environ.get('DATABASE_URL')


# Create a singleton instance
settings = Settings()