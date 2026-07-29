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

Analyze the logs strictly based on available evidence.

Rules:
- Use only information present in the logs and retrieved context.
- Do not speculate.
- If information is unknown, state "Unknown".
- Do not mention business or financial impacts unless clearly supported by the logs.
- Keep recommendations technical and actionable.

Determine:

1. Incident Type
2. Severity
3. Likely Root Cause
4. Evidence
5. Recommended Actions

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

    from app.incident_analyzer.parser import extract_events

    with open("logs/kubernetes_crashloop.log", "r") as f:
        log_text = f.read()

    events = extract_events(log_text)

    print("\nDetected Events:\n")

    for event in events:
        print(f"- {event}")

    print("\nGenerating Incident Report...\n")

    report = analyze(events)

    print(report)    