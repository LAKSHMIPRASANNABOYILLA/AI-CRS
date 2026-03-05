-- Initial schema for AI Code Review System
-- Run this script to initialize the database

CREATE TABLE IF NOT EXISTS reviews (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(255) NOT NULL,
    language    VARCHAR(50)  NOT NULL,
    code_snippet TEXT        NOT NULL,
    status      VARCHAR(20)  NOT NULL DEFAULT 'pending',
    result      TEXT,
    created_at  TIMESTAMP    NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS review_comments (
    id          SERIAL PRIMARY KEY,
    review_id   INTEGER      NOT NULL REFERENCES reviews(id) ON DELETE CASCADE,
    line_number INTEGER,
    severity    VARCHAR(20)  NOT NULL DEFAULT 'info',
    message     TEXT         NOT NULL,
    suggestion  TEXT,
    created_at  TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_review_comments_review_id ON review_comments(review_id);
CREATE INDEX IF NOT EXISTS idx_reviews_status ON reviews(status);
