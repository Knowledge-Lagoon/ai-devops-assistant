from pathlib import Path
import re

from app.rag.chat import ask_llm

from app.runbook_generator.prompts import (
    RUNBOOK_GENERATION_PROMPT
)

from app.runbook_generator.registry import (
    find_runbook_by_incident
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


def save_runbook(
    runbook: str,
    category: str,
    runbook_name: str
):

    output_dir = Path(
        f"runbooks/{category}"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        output_dir /
        f"{runbook_name}.md"
    )

    with open(
        output_file,
        "w"
    ) as f:

        f.write(runbook)

    return str(output_file)


if __name__ == "__main__":

    rca_file = input(
        "Enter RCA file path: "
    ).strip()

    category = input(
        "Enter category (kubernetes/cicd/terraform): "
    ).strip().lower()

    runbook_name = input(
        "Enter runbook name: "
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

    existing_runbook = (
        find_runbook_by_incident(
            incident_type
        )
    )

    if existing_runbook:

        print(
            "\nExisting runbook found:"
        )

        print(
            existing_runbook
        )

        print(
            "\nSkipping generation."
        )

    else:

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

        output_file = save_runbook(
            runbook,
            category,
            runbook_name
        )

        print(
            f"\nRunbook saved to: {output_file}"
        )