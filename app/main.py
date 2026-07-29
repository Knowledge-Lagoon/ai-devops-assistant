from app.ai.ollama_provider import OllamaProvider

def main():

    ai = OllamaProvider()

    print("\n1. DevOps Chat")
    print("2. Analyze Incident Log")

    choice = input("\nSelect option: ")

    if choice == "1":

        question = input("\nAsk me anything about DevOps: ")

        answer = ai.ask(question)

        print("\nAnswer:\n")
        print(answer)

    elif choice == "2":

        log_file = input("\nEnter log file path: ")

        # Incident Analyzer code here
