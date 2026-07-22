from app.ai.ollama_provider import OllamaProvider


def main() -> None:
    ai = OllamaProvider()
    question = input("Ask me anything about DevOps: ")
    answer = ai.ask(question)

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()