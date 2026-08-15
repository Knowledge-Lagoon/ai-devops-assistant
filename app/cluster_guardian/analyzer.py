from app.incident_analyzer.analyzer import (
    analyze_incident
)


def build_context(
    evidence: dict
):

    return f"""
Cluster:
{evidence['cluster']}

Namespace:
{evidence['namespace']}

Pod:
{evidence['pod']}

Timestamp:
{evidence['timestamp']}

Events:
{evidence['events']}

Current Logs:
{evidence['logs']}

Previous Logs:
{evidence['previous_logs']}

Deployments:
{evidence['deployments']}

Pod Description:
{evidence['describe']}
"""


def generate_rca(
    evidence: dict
):

    context = build_context(
        evidence
    )

    rca = analyze_incident(
        context
    )

    return rca


if __name__ == "__main__":

    sample_evidence = {
        "timestamp": "2026-08-15T20:00:00",
        "cluster": "eks-dev",
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