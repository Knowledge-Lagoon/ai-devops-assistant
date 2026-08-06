from app.cicd_assistant.log_parser import (
    extract_events
)

from app.rag.chat import ask_with_rag


def analyze_build_log(
    log_text
):

    events = extract_events(
        log_text
    )

    prompt = f"""
You are a Senior DevOps Engineer.

Analyze the CI/CD failure strictly using the evidence provided.

Rules:

- Use only the log evidence and retrieved RAG context.
- Do not speculate.
- Do not assume tools, platforms, or environments not present in the logs.
- If information is unknown, state "Unknown".
- Ground recommendations in the evidence.

Provide:

Incident Type:
Severity:
Likely Root Cause:
Evidence:
Recommended Actions:

Build Log Events:

{chr(10).join(events)}
"""

    return ask_with_rag(
        prompt
    )


if __name__ == "__main__":

    with open(
        "logs/cicd/jenkins_build_failure.log",
        "r"
    ) as f:

        log_text = f.read()

    print(
        analyze_build_log(
            log_text
        )
    )