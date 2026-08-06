from app.rag.chat import ask_with_rag

from app.cicd_assistant.prompts import (
    PIPELINE_REVIEW_PROMPT
)


def analyze_pipeline(
    pipeline_text: str
):

    prompt = PIPELINE_REVIEW_PROMPT.format(
        pipeline=pipeline_text
    )

    return ask_with_rag(prompt)


if __name__ == "__main__":

    pipeline_file = input(
        "Enter pipeline file path: "
    ).strip()

    with open(
        pipeline_file,
        "r"
    ) as f:

        pipeline = f.read()

    print(
        analyze_pipeline(
            pipeline
        )
    )