"""
Log parser for AI Incident Analyzer.
"""

ERROR_KEYWORDS = [
    "ERROR",
    "Error",
    "Exception",
    "Failed",
    "FAILURE",
    "Timeout",
    "CrashLoopBackOff",
    "ImagePullBackOff",
    "ErrImagePull",
    "OOMKilled",
    "Exit Code",
    "Back-off",
    "Terminated",
    "Reason:",
    "Connection refused",
    "Connection timeout",
    "Unable to connect",
    "Build failed",
    "Deployment failed",
]


def extract_events(log_text: str) -> list[str]:

    events = []

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

    events = extract_events(log_text)

    return {
        "total_lines": len(log_text.splitlines()),
        "event_count": len(events),
        "events": events,
    }


if __name__ == "__main__":

    sample_log = """
ERROR JDBC Connection Timeout
ERROR Connection pool exhausted
INFO Application started
ERROR Unable to connect to database
"""

    events = extract_events(sample_log)

    print("Detected Events:")

    for event in events:
        print(event)