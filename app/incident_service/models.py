def build_incident(
    pod: dict,
    evidence: dict,
    rca: str,
    runbook: dict = None
):

    return {
        "cluster": pod["cluster"],
        "namespace": pod["namespace"],
        "pod": pod["pod"],
        "container": pod.get(
            "container"
        ),
        "incident_type": pod["reason"],
        "severity": pod.get(
            "severity_hint",
            "Unknown"
        ),
        "evidence": {
            "logs": evidence.get(
                "logs"
            ),
            "previous_logs": evidence.get(
                "previous_logs"
            ),
            "events": evidence.get(
                "events"
            )
        },
        "rca": rca,
        "runbook": runbook
    }