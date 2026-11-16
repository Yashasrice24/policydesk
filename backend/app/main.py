
from fastapi import FastAPI

app = FastAPI(
    title="PolicyDesk API",
    description="AI-powered RAG Document Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PolicyDesk API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
