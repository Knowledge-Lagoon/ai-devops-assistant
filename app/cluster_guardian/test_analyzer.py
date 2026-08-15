from app.cluster_guardian.collector import (
    get_failed_pods,
    collect_evidence
)

from app.cluster_guardian.analyzer import (
    generate_rca
)

CLUSTER_CONTEXT = "eks-dev"

failed_pods = get_failed_pods(
    CLUSTER_CONTEXT
)

if not failed_pods:

    print(
        "No failed pods found"
    )

    exit(0)

pod = failed_pods[0]

evidence = collect_