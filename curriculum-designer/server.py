"""
server.py

FastAPI server for Curriculum Designer MVP
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ai_backend import generate_curriculum


# -------------------------------------------------------
# FastAPI App
# -------------------------------------------------------

app = FastAPI(
    title="Curriculum Designer API",
    version="0.1",
    description="LLM-powered Curriculum Designer"
)


# -------------------------------------------------------
# Request Model
# -------------------------------------------------------

class CurriculumRequest(BaseModel):
    subject: str
    target_audience: str
    prerequisites: str
    duration: int


# -------------------------------------------------------
# Health Check
# -------------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Curriculum Designer API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


# -------------------------------------------------------
# Generate Curriculum
# -------------------------------------------------------

@app.post("/generate")
def generate(request: CurriculumRequest):

    try:

        curriculum = generate_curriculum(
            subject=request.subject,
            target_audience=request.target_audience,
            prerequisites=request.prerequisites,
            duration=request.duration,
        )

        return curriculum

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )