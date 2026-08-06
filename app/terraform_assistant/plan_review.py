from app.rag.chat import ask_with_rag

from app.terraform_assistant.prompts import (
    TERRAFORM_PLAN_REVIEW_PROMPT
)


def analyze_plan(plan_text):

    prompt = TERRAFORM_PLAN_REVIEW_PROMPT.format(
        plan=plan_text
    )

    return ask_with_rag(prompt)


if __name__ == "__main__":

    plan_file = input(
        "Enter Terraform plan file: "
    ).strip()

    with open(
        plan_file,
        "r"
    ) as f:

        plan_text = f.read()

    print(
        analyze_plan(
            plan_text
        )
    )