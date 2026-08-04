from app.incident_analyzer.parser import extract_events
from app.incident_analyzer.analyzer import analyze

from app.kubernetes_assistant.cluster_analyzer import (
    get_pod_details,
    get_pod_logs,
)


def analyze_pod(pod_name, pod_details=None, pod_logs=None, namespace="chaos-lab"):
    if pod_details is None:
        pod_details = get_pod_details(pod_name, namespace=namespace)
    if pod_logs is None:
        pod_logs = get_pod_logs(pod_name, namespace=namespace)

    combined = f"""
=== POD DETAILS ===

{pod_details}

=== POD LOGS ===

{pod_logs}
"""

    events = extract_events(combined)
    return analyze(events)


if __name__ == "__main__":
    pod_name = input("Enter pod name: ").strip()
    namespace = input("Enter namespace [chaos-lab]: ").strip() or "chaos-lab"

    print("Would you like to provide pod describe/log output manually? (y/N)")
    choice = input().strip().lower()

    if choice in {"y", "yes"}:
        print("Paste pod describe output (end with EOF on a new line):")
        pod_details_lines = []
        while True:
            line = input()
            if line == "EOF":
                break
            pod_details_lines.append(line)
        pod_details = "\n".join(pod_details_lines)

        print("Paste pod logs output (end with EOF on a new line):")
        pod_logs_lines = []
        while True:
            line = input()
            if line == "EOF":
                break
            pod_logs_lines.append(line)
        pod_logs = "\n".join(pod_logs_lines)

        report = analyze_pod(pod_name, pod_details=pod_details, pod_logs=pod_logs, namespace=namespace)
    else:
        report = analyze_pod(pod_name, namespace=namespace)

    print(report)