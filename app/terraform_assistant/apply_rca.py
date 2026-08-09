from app.terraform_assistant.log_parser import (
    extract_events
)

from app.rag.chat import ask_with_rag


def analyze_apply_failure(log_text):

    events = extract_events(
        log_text
    )

    evidence = "\n".join(events)

    prompt = f"""
You are a Senior Cloud Architect.

Analyze the Terraform apply failure.

Use only the evidence and retrieved Terraform knowledge.

Provide:

Incident Type:
Severity:
Likely Root Cause:
Evidence:
Recommended Actions:

Terraform Apply Failure Events:

{evidence}
"""

    return ask_with_rag(
        prompt,
        retrieval_query=evidence
    )


if __name__ == "__main__":

    log_file = input(
        "Enter Terraform failure log path: "
    ).strip()

    with open(
        log_file,
        "r"
    ) as f:

        log_text = f.read()

    print(
        analyze_apply_failure(
            log_text
        )
    )