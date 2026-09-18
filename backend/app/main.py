
from fastapi import FastAPI

app = FastAPI(
    title="KnowledgePilot API",
    description="Backend API for KnowledgePilot",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "KnowledgePilot API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }