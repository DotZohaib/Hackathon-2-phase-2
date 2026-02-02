import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Todo App Phase II"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changethis_secret_key_extremely_insecure_for_dev")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000"]

settings = Settings()
