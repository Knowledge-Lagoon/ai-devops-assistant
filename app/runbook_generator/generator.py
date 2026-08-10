from pathlib import Path

from app.rag.chat import ask_with_rag

from app.runbook_generator.prompts import (
    RUNBOOK_GENERATION_PROMPT
)


def generate_runbook(
    rca_text: str
) -> str:

    prompt = RUNBOOK_GENERATION_PROMPT.format(
        rca=rca_text
    )

    return ask_with_rag(
        prompt,
        retrieval_query=rca_text
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

        f.write(
            runbook
        )

    return str(
        output_file
    )


if __name__ == "__main__":

    rca_file = input(
        "Enter RCA file path: "
    ).strip()

    category = input(
        "Enter category "
        "(kubernetes/cicd/terraform): "
    ).strip().lower()

    runbook_name = input(
        "Enter runbook name: "
    ).strip()

    with open(
        rca_file,
        "r"
    ) as f:

        rca_text = f.read()

    print(
        "\nGenerating runbook...\n"
    )

    runbook = generate_runbook(
        rca_text
    )

    print(
        "\n===== GENERATED RUNBOOK =====\n"
    )

    print(
        runbook
    )

    output_file = save_runbook(
        runbook,
        category,
        runbook_name
    )

    print(
        f"\nRunbook saved to: "
        f"{output_file}"
    )