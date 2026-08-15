import json

from app.cluster_guardian.collector import (
    get_failed_pods,
    collect_evidence
)

CLUSTER_CONTEXT = (
    "arn:aws:eks:us-east-1:275198336814:cluster/k8s-chaos-lab"
)

failed_pods = get_failed_pods(
    CLUSTER_CONTEXT
)

print(
    "\n=== FAILED PODS ===\n"
)

print(
    json.dumps(
        failed_pods,
        indent=2
    )
)

if failed_pods:

    pod = failed_pods[0]

    evidence = collect_evidence(
        context=pod["cluster"],
        namespace=pod["namespace"],
        pod=pod["pod"]
    )

    print(
        "\n=== EVIDENCE ===\n"
    )

    print(
        json.dumps(
            evidence,
            indent=2
        )
    )

else:

    print(
        "\nNo failed pods found.\n"
    )