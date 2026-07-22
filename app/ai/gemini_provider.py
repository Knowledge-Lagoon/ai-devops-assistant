from google import genai
from app.config import GEMINI_API_KEY
from app.ai.base import AIProvider


class GeminiProvider(AIProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def ask(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text