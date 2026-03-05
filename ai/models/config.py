"""Supported AI model configurations for AI-CRS."""

SUPPORTED_MODELS = {
    "gpt-4o": {
        "provider": "openai",
        "context_window": 128000,
        "description": "Most capable GPT-4 model, best for complex reviews",
    },
    "gpt-4o-mini": {
        "provider": "openai",
        "context_window": 128000,
        "description": "Faster and cheaper, suitable for smaller code snippets",
    },
    "gpt-3.5-turbo": {
        "provider": "openai",
        "context_window": 16385,
        "description": "Fast and cost-effective for simple reviews",
    },
}

DEFAULT_MODEL = "gpt-4o"
