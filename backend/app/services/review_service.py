from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.review import Review, ReviewComment, ReviewStatus
from app.schemas.review import ReviewCreateRequest
from app.services.ai_service import ai_service


class ReviewService:
    def create_review(self, db: Session, request: ReviewCreateRequest) -> Review:
        review = Review(
            title=request.title,
            language=request.language,
            code_snippet=request.code_snippet,
            status=ReviewStatus.PENDING,
        )
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    def run_ai_review(self, db: Session, review: Review) -> Review:
        review.status = ReviewStatus.IN_PROGRESS
        db.commit()

        try:
            ai_result = ai_service.review_code(review.code_snippet, review.language)

            review.result = ai_result.get("summary", "")
            review.status = ReviewStatus.COMPLETED

            for comment_data in ai_result.get("comments", []):
                comment = ReviewComment(
                    review_id=review.id,
                    line_number=comment_data.get("line_number"),
                    severity=comment_data.get("severity", "info"),
                    message=comment_data.get("message", ""),
                    suggestion=comment_data.get("suggestion"),
                )
                db.add(comment)

        except Exception as e:
            review.status = ReviewStatus.FAILED
            review.result = f"Review failed: {str(e)}"

        db.commit()
        db.refresh(review)
        return review

    def get_review(self, db: Session, review_id: int) -> Optional[Review]:
        return db.query(Review).filter(Review.id == review_id).first()

    def list_reviews(self, db: Session, skip: int = 0, limit: int = 20) -> List[Review]:
        return db.query(Review).offset(skip).limit(limit).all()


review_service = ReviewService()
