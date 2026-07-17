"""Application Configuration"""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    app_title: str = "GRC Platform API"
    app_version: str = "1.0.0"
    app_description: str = "Integrated Governance, Risk & Compliance Platform"
    debug: bool = False
    environment: str = "development"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # Database
    database_url: str = "postgresql://grc_user:grc_password@localhost:5432/grcdb"
    database_echo: bool = False

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # JWT
    secret_key: str = "your-super-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # Keycloak
    keycloak_server_url: str = "http://localhost:8080"
    keycloak_realm: str = "grc"
    keycloak_client_id: str = "grc-app"
    keycloak_client_secret: str = "secret"

    # Ollama (AI)
    ollama_api_url: str = "http://localhost:11434"
    ollama_model: str = "llama2"
    ollama_temperature: float = 0.7
    ollama_max_tokens: int = 1000

    # CORS
    cors_origins: list = ["http://localhost:3000", "http://localhost:8000"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_headers: list = ["*"]

    # Logging
    log_level: str = "INFO"
    log_file: Optional[str] = "logs/app.log"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
