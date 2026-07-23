import os

import ollama

from app.ai.base import AIProvider


class OllamaProvider(AIProvider):
    def __init__(self, model: str | None = None, host: str | None = None):
        self.model = model or os.getenv("OLLAMA_MODEL", "phi3:mini")
        self.host = host or os.getenv("OLLAMA_HOST", "http://172.31.15.13:11434")

    def ask(self, prompt: str) -> str:
        client = ollama.Client(host=self.host)
        response = client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]