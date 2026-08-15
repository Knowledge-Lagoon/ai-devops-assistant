failed_pods = get_failed_pods(
    context
)

for pod in failed_pods:

    evidence = collect_evidence(
        context=context,
        namespace=pod["namespace"],
        pod=pod["pod"]
    )

    rca = generate_rca(
        evidence
    )

    runbook = get_or_create_runbook(
        incident_type,
        rca
    )