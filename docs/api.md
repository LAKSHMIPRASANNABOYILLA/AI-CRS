# API Reference

Base URL: `http://localhost:8000/api/v1`

Interactive docs: `http://localhost:8000/docs`

---

## Health

### GET /health

Returns service health status.

**Response 200**
```json
{ "status": "ok", "service": "AI-CRS Backend" }
```

---

## Reviews

### POST /reviews

Submit code for AI review.

**Request Body**
```json
{
  "title": "My function review",
  "language": "python",
  "code_snippet": "def foo(): pass"
}
```

**Response 201**
```json
{
  "id": 1,
  "title": "My function review",
  "language": "python",
  "status": "pending",
  "created_at": "2024-01-01T00:00:00Z"
}
```

---

### GET /reviews

List all reviews (paginated).

**Query Parameters**
- `skip` (int, default 0)
- `limit` (int, default 20)

---

### GET /reviews/{id}

Get a specific review with all AI comments.

**Response 200**
```json
{
  "id": 1,
  "title": "My function review",
  "language": "python",
  "status": "completed",
  "result": "Overall looks good...",
  "comments": [
    {
      "line_number": 3,
      "severity": "warning",
      "message": "Missing type hints",
      "suggestion": "Add `-> None` return type annotation"
    }
  ],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:01Z"
}
```
