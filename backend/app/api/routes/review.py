from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db, SessionLocal
from app.schemas.review import ReviewCreateRequest, ReviewResponse, ReviewSummary
from app.services.review_service import review_service

router = APIRouter()


def _run_review_in_background(review_id: int) -> None:
    """Run AI review in a fresh DB session (safe for background tasks)."""
    db = SessionLocal()
    try:
        review = review_service.get_review(db, review_id)
        if review:
            review_service.run_ai_review(db, review)
    finally:
        db.close()


@router.post("/reviews", response_model=ReviewSummary, status_code=201)
def create_review(
    request: ReviewCreateRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    review = review_service.create_review(db, request)
    background_tasks.add_task(_run_review_in_background, review.id)
    return review


@router.get("/reviews", response_model=List[ReviewSummary])
def list_reviews(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return review_service.list_reviews(db, skip=skip, limit=limit)


@router.get("/reviews/{review_id}", response_model=ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = review_service.get_review(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review
