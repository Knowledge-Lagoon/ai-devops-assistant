from app.incident_analyzer.analyzer import (
    analyze
)


def build_log_events(
    evidence: dict
):

    return [
        evidence["events"],
        evidence["logs"],
        evidence["previous_logs"],
        evidence["describe"]
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
        "timestamp": "2026-08-15T20:00:00",
        "cluster": "k8s-chaos-lab",
        "namespace": "default",
        "pod": "test-pod",
        "events": "Back-off restarting failed container",
        "logs": "Application startup failed",
        "previous_logs": "Database connection refused",
        "deployments": "sample deployment",
        "describe": "CrashLoopBackOff"
    }

    rca = generate_rca(
        sample_evidence
    )

    print(
        "\n=== RCA ===\n"
    )

    print(rca)