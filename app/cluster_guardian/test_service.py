from app.cluster_guardian.service import (
    process_cluster
)

CLUSTER_CONTEXT = (
    "arn:aws:eks:us-east-1:599626541016:cluster/k8s-chaos-lab"
)

results = process_cluster(
    CLUSTER_CONTEXT
)

print(
    "\n=== RESULTS ===\n"
)

for result in results:

    print(
        f"Pod: {result['pod']}"
    )

    print(
        f"Incident: {result['incident_type']}"
    )

    print(
        f"Runbook: {result['runbook']}"
    )

    print() 