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

Perform a CI/CD failure RCA.

Evidence:

{chr(10).join(events)}

Provide:

1. Incident Type
2. Severity
3. Root Cause
4. Evidence
5. Recommended Actions
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