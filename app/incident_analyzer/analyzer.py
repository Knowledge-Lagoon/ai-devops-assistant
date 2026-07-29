"""
AI Incident Analyzer

Uses the existing RAG pipeline to:
1. Search the DevOps knowledge base
2. Analyze log events
3. Generate an incident report
"""

from app.rag.chat import ask_with_rag


def analyze(log_events: list[str]) -> str:
    """
    Analyze extracted log events using RAG.

    Args:
        log_events: List of important log entries from parser.py

    Returns:
        AI-generated incident analysis report
    """

    if not log_events:
        return (
            "No significant errors were detected in the log file.\n"
            "Try providing a log containing ERROR, Exception, "
            "Timeout, CrashLoopBackOff, or similar events."
        )

    events_text = "\n".join(
        f"- {event}"
        for event in log_events
    )

    prompt = f"""
You are a Senior DevOps Engineer and Site Reliability Engineer.

Analyze the following incident logs.

Determine:

1. Incident Type
2. Severity
3. Likely Root Cause
4. Business Impact
5. Recommended Actions

Rules:

- Base conclusions only on the provided logs and retrieved context.
- If information is not available, say "Unknown".
- Do not invent shell commands.
- Do not generate kubectl, terraform, Jenkins, SQL, or Linux commands unless they are explicitly supported by the retrieved context.
- Keep recommendations practical and concise.

Log Events:

{events_text}

Provide the response in the following format:

Incident Type:
<value>

Severity:
<value>

Likely Root Cause:
<value>

Business Impact:
<value>

Recommended Actions:
- action 1
- action 2
- action 3
"""

    return ask_with_rag(prompt)


if __name__ == "__main__":

    sample_events = [
        "ERROR JDBC Connection Timeout",
        "ERROR Connection pool exhausted",
        "ERROR Unable to connect to database",
    ]

    print(
        analyze(sample_events)
    )