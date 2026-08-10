from app.rag.chat import ask_with_rag

from app.runbook_generator.prompts import (
    RUNBOOK_GENERATION_PROMPT
)


def generate_runbook(
    rca_text
):

    prompt = RUNBOOK_GENERATION_PROMPT.format(
        rca=rca_text
    )

    return ask_with_rag(
        prompt,
        retrieval_query=rca_text
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

    runbook = generate_runbook(
        rca_text
    )

    print(runbook)