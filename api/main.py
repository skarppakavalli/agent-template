
from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="AI Hackathon API",
    description="Reusable GenAI application backend",
    version="1.0.0"
)

# Register API routes
app.include_router(router)
