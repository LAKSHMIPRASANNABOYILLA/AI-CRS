MAX_CODE_LENGTH = 10_000  # characters


def truncate_code(code: str, max_length: int = MAX_CODE_LENGTH) -> str:
    """Truncate code to fit within model context limits."""
    if len(code) <= max_length:
        return code
    return code[:max_length] + "\n# ... (truncated)"


def detect_language(filename: str) -> str:
    """Detect programming language from file extension."""
    extension_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".go": "go",
        ".rs": "rust",
        ".cpp": "cpp",
        ".c": "c",
        ".cs": "csharp",
        ".rb": "ruby",
        ".php": "php",
    }
    for ext, lang in extension_map.items():
        if filename.endswith(ext):
            return lang
    return "text"
