from app.ai.ollama_provider import OllamaProvider

from app.incident_analyzer.parser import extract_events
from app.incident_analyzer.analyzer import analyze


def main():

    print("\n=== AI DevOps Assistant ===")
    print("1. Ask DevOps Question")
    print("2. Analyze Incident Log")
    print("3. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":

        ai = OllamaProvider()

        question = input(
            "\nAsk me anything about DevOps: "
        )

        answer = ai.ask(question)

        print("\nAnswer:\n")
        print(answer)

    elif choice == "2":

        log_file = input(
            "\nEnter log file path: "
        )

        try:

            with open(log_file, "r") as f:
                log_text = f.read()

            events = extract_events(log_text)

            print("\nDetected Events:\n")

            for event in events:
                print(f"- {event}")

            print("\nGenerating Incident Report...\n")

            report = analyze(events)

            print(report)

        except FileNotFoundError:

            print(
                f"\nLog file not found: {log_file}"
            )

    elif choice == "3":

        print("Goodbye!")

    else:

        print("Invalid selection")


if __name__ == "__main__":
    main()