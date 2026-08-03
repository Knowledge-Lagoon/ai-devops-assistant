from app.incident_analyzer.parser import extract_events
from app.incident_analyzer.analyzer import analyze

from app.kubernetes_assistant.cluster_analyzer import (
    get_pod_details,
    get_pod_logs
)


def analyze_pod(pod_name):

    pod_details = get_pod_details(pod_name)

    pod_logs = get_pod_logs(pod_name)

    combined = f"""
=== POD DETAILS ===

{pod_details}

=== POD LOGS ===

{pod_logs}
"""

    events = extract_events(combined)

    return analyze(events)

if __name__ == "__main__":

    pod_name = input(
        "Enter pod name: "
    )

    report = analyze_pod(
        pod_name
    )

    print(report)