from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from app.models.review import ReviewStatus, ReviewSeverity


class ReviewCommentSchema(BaseModel):
    line_number: Optional[int] = None
    severity: ReviewSeverity = ReviewSeverity.INFO
    message: str
    suggestion: Optional[str] = None


class ReviewCreateRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    language: str = Field(..., min_length=1, max_length=50)
    code_snippet: str = Field(..., min_length=1)


class ReviewResponse(BaseModel):
    id: int
    title: str
    language: str
    status: ReviewStatus
    result: Optional[str] = None
    comments: List[ReviewCommentSchema] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ReviewSummary(BaseModel):
    id: int
    title: str
    language: str
    status: ReviewStatus
    created_at: datetime

    class Config:
        from_attributes = True
