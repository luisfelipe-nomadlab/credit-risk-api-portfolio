from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "Real time fraud detection"
    DEBUG: bool = False

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None  

    # MLOps / tracking
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MLFLOW_EXPERIMENT_NAME: str = "fraud_detection"

    # Outros
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
