import re

from app.rag.chat import ask_llm

from app.runbook_service.prompts import (
    RUNBOOK_GENERATION_PROMPT
)


def extract_incident_type(
    rca_text: str
) -> str:

    match = re.search(
        r"Incident Type:\s*(.+)",
        rca_text,
        re.IGNORECASE
    )

    if match:

        return match.group(1).strip()

    return "Unknown"


def generate_runbook(
    rca_text: str
) -> str:

    prompt = RUNBOOK_GENERATION_PROMPT.format(
        rca=rca_text
    )

    return ask_llm(
        prompt
    )


if __name__ == "__main__":

    rca_file = input(
        "Enter RCA file path: "
    ).strip()

    with open(
        rca_file,
        "r"
    ) as f:

        rca_text = f.read()

    incident_type = extract_incident_type(
        rca_text
    )

    print(
        f"\nIncident Type: {incident_type}"
    )

    print(
        "\nGenerating runbook...\n"
    )

    runbook = generate_runbook(
        rca_text
    )

    print(
        "\n===== GENERATED RUNBOOK =====\n"
    )

    print(runbook)