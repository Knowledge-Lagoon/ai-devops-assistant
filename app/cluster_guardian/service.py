from app.cluster_guardian.collector import (
    get_failed_pods,
    collect_evidence
)

from app.cluster_guardian.analyzer import (
    generate_rca
)

from app.runbook_service.service import (
    get_or_create_runbook
)


def process_cluster(
    context: str
):

    failed_pods = get_failed_pods(
        context
    )

    if not failed_pods:

        print(
            "\nNo failed pods found.\n"
        )

        return

    for pod in failed_pods:

        print(
            f"\nProcessing pod: "
            f"{pod['pod']}\n"
        )

        evidence = collect_evidence(
            context=context,
            namespace=pod["namespace"],
            pod=pod["pod"]
        )

        rca = generate_rca(
            evidence
        )

        incident_type = pod.get(
            "reason",
            "Unknown"
        )

        runbook = get_or_create_runbook(
            incident_type=incident_type,
            rca_text=rca
        )

        print(
            "\n=== RUNBOOK RESULT ===\n"
        )

        print(
            runbook
        )