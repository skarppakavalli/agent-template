
import os
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv()


class Settings:

    # LLM configuration
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_MODEL = os.getenv(
        "GOOGLE_MODEL", "gemini-2.5-flash"
    )

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv(
        "GROQ_MODEL", "llama-3.3-70b-versatile"
    )

    # LangSmith
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Hugging Face
    HF_TOKEN = os.getenv("HF_TOKEN")

    APP_ENV = os.getenv("APP_ENV", "development")


settings = Settings()
