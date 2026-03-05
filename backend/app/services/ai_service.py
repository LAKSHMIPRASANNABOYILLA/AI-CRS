import openai
import json
from app.core.config import settings

REVIEW_SYSTEM_PROMPT = """You are an expert code reviewer. Analyze the provided code and return a JSON response with:
- summary: a brief overall assessment
- comments: a list of issues, each with:
  - line_number (int or null)
  - severity: one of "info", "warning", "error", "critical"
  - message: description of the issue
  - suggestion: how to fix it (or null)

Focus on: bugs, security vulnerabilities, performance issues, code style, and best practices."""


class AIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    def review_code(self, code_snippet: str, language: str) -> dict:
        prompt = f"Review the following {language} code:\n\n```{language}\n{code_snippet}\n```"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": REVIEW_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.2,
        )

        return json.loads(response.choices[0].message.content)


ai_service = AIService()
