import os

from .base import AIProvider


class GeminiProvider(AIProvider):
    """Simple Gemini-backed provider implementation."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY", "")

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set")

        return f"Gemini provider received prompt: {prompt}"
