from fastapi import FastAPI

from backend.routes.projects import router as projects_router
from backend.routes.skills import router as skills_router
from backend.routes.profile import router as profile_router


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