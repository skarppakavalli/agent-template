# AI Hackathon Starter

Reusable Python GenAI application template.

## Technology Stack

- Python
- LangChain
- LangGraph
- Gemini / Groq
- LangSmith
- Hugging Face
- FastAPI
- Streamlit
- PostgreSQL

## Setup

### 1. Install dependencies

uv sync

### 2. Configure environment

Copy .env.example to .env.

Add your API keys.

### 3. Start FastAPI

uv run uvicorn api.main:app --reload

### 4. Start Streamlit

uv run streamlit run frontend/streamlit_app.py

### 5. Run tests

uv run pytest -v

## API Documentation

http://127.0.0.1:8000/docs
