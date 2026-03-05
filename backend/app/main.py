from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health, review
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered Automatic Code Review System API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(review.router, prefix="/api/v1", tags=["review"])


@app.get("/")
def root():
    return {"message": "AI Code Review System API", "docs": "/docs"}
