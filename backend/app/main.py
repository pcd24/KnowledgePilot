from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db
app = FastAPI(
    title="KnowledgePilot API",
    description="Backend API for KnowledgePilot",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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
    
@app.get("/db-test")
def db_test():
    return {
        "database": db.name,
        "status": "connected"
    }