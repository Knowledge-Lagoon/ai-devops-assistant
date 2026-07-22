from app.ai.gemini_provider import GeminiProvider

ai = GeminiProvider()

question = input("Ask me anything about DevOps: ")

answer = ai.ask(question)

print("\nAnswer:\n")
print(answer)