from fastapi import FastAPI

from app.ai.gemini_provider import GeminiProvider

app = FastAPI(title="AI DevOps Assistant")
provider = GeminiProvider()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "AI DevOps Assistant is running"}


@app.post("/generate")
def generate(prompt: str) -> dict[str, str]:
    return {"response": provider.generate(prompt)}
