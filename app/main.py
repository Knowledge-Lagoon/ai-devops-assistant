from app.ai.gemini_provider import GeminiProvider


def main() -> None:
    ai = GeminiProvider()
    question = input("Ask me anything about DevOps: ")
    answer = ai.ask(question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()