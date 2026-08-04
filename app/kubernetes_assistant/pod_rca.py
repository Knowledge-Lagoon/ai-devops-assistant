from app.incident_analyzer.parser import extract_events
from app.incident_analyzer.analyzer import analyze

from app.kubernetes_assistant.cluster_analyzer import (
    get_pod_details,
    get_pod_logs
)


def analyze_pod(
    pod_name,
    namespace="chaos-lab"
):

    print(
        f"\nCollecting information for pod '{pod_name}' "
        f"in namespace '{namespace}'...\n"
    )

    pod_details = get_pod_details(
        pod_name,
        namespace
    )

    pod_logs = get_pod_logs(
        pod_name,
        namespace
    )

    combined = f"""
=== POD DETAILS ===

{pod_details}

=== POD LOGS ===

{pod_logs}
"""

    events = extract_events(
        combined
    )

    print("\n===== EXTRACTED EVENTS =====\n")

    if events:

        for event in events:
            print(event)

    else:

        print(
            "No events were extracted."
        )

    print(
        f"\nTotal Events Found: "
        f"{len(events)}\n"
    )

    report = analyze(
        events
    )

    return report


if __name__ == "__main__":

    pod_name = input(
        "Enter pod name: "
    ).strip()

    report = analyze_pod(
        pod_name,
        "chaos-lab"
    )

    print(
        "\n===== AI INCIDENT REPORT =====\n"
    )

    print(report)