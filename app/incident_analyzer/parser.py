"""
Log parser for AI Incident Analyzer.

Extracts important error and warning events from logs
before sending them to the RAG pipeline.
"""

ERROR_KEYWORDS = [
    "ERROR",
    "Exception",
    "Failed",
    "FAILURE",
    "Timeout",
    "CrashLoopBackOff",
    "OOMKilled",
    "Connection refused",
    "Connection timeout",
    "Unable to connect",
    "Build failed",
    "Deployment failed"
]


def extract_events(log_text: str) -> list[str]:
    """
    Extract significant log entries.

    Args:
        log_text: Raw log file contents

    Returns:
        List of relevant log lines
    """

   ]

    for line in log_text.splitlines():

        line = line.strip()

        if not line:
            continue

        if any(
            keyword.lower() in line.lower()
            for keyword in ERROR_KEYWORDS
        ):
            events.append(line)

    return events


def summarize_log(log_text: str) -> dict:
    """
    Create a basic summary of a log file.

    Returns:
        Dictionary containing statistics and events.
    """

    events = extract_events(log_text)

    return {
        "total_lines": len(log_text.splitlines()),
        "event_count": len(events),
        "events": events
    }


if __name__ == "__main__":

    sample_log = """
    ERROR JDBC Connection Timeout
    ERROR Connection pool exhausted
    INFO Application started
    ERROR Unable to connect to database
    """

    results = extract_events(sample_log)

    print("Detected Events:")
    for event in results:
        print(event)
``