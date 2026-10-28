from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from backend.routes.projects import router as projects_router
from backend.routes.skills import router as skills_router
from backend.routes.profile import router as profile_router
from backend.services.llm_service import generate_answer


app = FastAPI(
    title="Prashant Kumar Portfolio API",
    description="Backend API for my AI Engineer portfolio",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Prashant Kumar Portfolio API",
        "status": "running",
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    projects_router,
    prefix="/api"
)

app.include_router(
    skills_router,
    prefix="/api"
)

app.include_router(
    profile_router,
    prefix="/api"
)


#Code for AI Chatbot API endpoint

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=2000)


class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    history: list[ChatMessage] = Field(default_factory=list, max_length=10)


class ChatResponse(BaseModel):
    question: str
    answer: str


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = generate_answer(
            request.question.strip(),
            history=[message.model_dump() for message in request.history],
        )

        return ChatResponse(
            question=request.question.strip(),
            answer=answer,
        )

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="The AI service is temporarily unavailable. Please try again.",
        )