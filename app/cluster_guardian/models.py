def build_incident(
    pod,
    evidence,
    rca,
    runbook
):

    return {
        "cluster": pod["cluster"],
        "namespace": pod["namespace"],
        "pod": pod["pod"],
        "incident_type": pod["reason"],
        "severity": pod["severity_hint"],
        "rca": rca,
        "runbook": runbook
    }