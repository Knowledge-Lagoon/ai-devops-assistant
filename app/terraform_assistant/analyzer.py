from app.rag.chat import ask_with_rag

from app.terraform_assistant.prompts import (
    TERRAFORM_REVIEW_PROMPT
)


def analyze_terraform(terraform_text):

    prompt = TERRAFORM_REVIEW_PROMPT.format(
        terraform=terraform_text
    )

    return ask_with_rag(
        prompt
    )


if __name__ == "__main__":

    terraform_file = input(
        "Enter Terraform file path: "
    ).strip()

    with open(
        terraform_file,
        "r"
    ) as f:

        terraform_text = f.read()

    print(
        analyze_terraform(
            terraform_text
        )
    )