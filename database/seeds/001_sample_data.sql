-- Sample seed data for development/testing
INSERT INTO reviews (title, language, code_snippet, status, result) VALUES
(
    'Sample Python Review',
    'python',
    'def add(a, b):\n    return a + b\n\nprint(add(1, 2))',
    'completed',
    'Simple addition function. No major issues found.'
);
