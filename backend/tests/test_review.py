from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_review_validation():
    # Missing required fields should return 422
    response = client.post("/api/v1/reviews", json={})
    assert response.status_code == 422


def test_get_review_not_found():
    with patch("app.api.routes.review.review_service.get_review", return_value=None):
        response = client.get("/api/v1/reviews/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Review not found"


def test_list_reviews_empty():
    with patch("app.api.routes.review.review_service.list_reviews", return_value=[]):
        response = client.get("/api/v1/reviews")
        assert response.status_code == 200
        assert response.json() == []
