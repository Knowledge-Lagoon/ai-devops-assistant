import os

from google import genai

from app.ai.base import AIProvider
from app.config import GEMINI_API_KEY


class GeminiProvider(AIProvider):
    def __init__(self, api_key: str | None = None):
        resolved_api_key = api_key or GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")
        if not resolved_api_key:
            raise ValueError("GEMINI_API_KEY is not set")

        self.client = genai.Client(api_key=resolved_api_key)

    def ask(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text