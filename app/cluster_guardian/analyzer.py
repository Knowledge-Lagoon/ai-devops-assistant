from app.incident_analyzer.analyzer import (
    analyze
)


def build_log_events(
    evidence: dict
):

    incident_type = evidence.get(
        "incident_type",
        "Unknown"
    )

    summary = f"""
Incident Type:
{incident_type}

Current Logs:
{evidence["logs"]}

Previous Logs:
{evidence["previous_logs"]}

Recent Events:
{evidence["events"]}
"""

    return [
        summary
    ]


def generate_rca(
    evidence: dict
):

    log_events = build_log_events(
        evidence
    )

    rca = analyze(
        log_events
    )

    return rca


if __name__ == "__main__":

    sample_evidence = {
        "incident_type": "CrashLoopBackOff",
        "logs": (
            "Database connection failed\n"
            "Unable to connect to postgres-service"
        ),
        "previous_logs": (
            "Database connection failed\n"
            "Unable to connect to postgres-service"
        ),
        "events": (
            "Back-off restarting failed container"
        )
    }

    rca = generate_rca(
        sample_evidence
    )

    print(
        "\n=== RCA ===\n"
    )

    print(rca)