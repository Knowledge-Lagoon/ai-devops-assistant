import time
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

start = time.time()

def process_cluster(
    context: str
):

    print(
        f"\n=== PROCESSING CLUSTER: {context} ===\n"
    )

    failed_pods = get_failed_pods(
        context
    )

    if not failed_pods:

        print(
            "\nNo failed pods found.\n"
        )

        return []

    results = []

    for pod in failed_pods:

        print(
            f"\nProcessing pod: "
            f"{pod['pod']}"
        )

        evidence = collect_evidence(
            context=context,
            namespace=pod["namespace"],
            pod=pod["pod"]
        )
        
        start = time.time()
        print("Generating RCA")
        rca = generate_rca(
            evidence
        )


        print(
            f"RCA completed in "
            f"{time.time() - start:.2f}s"
)

        print("Searching / Creating Runbook")
        runbook = get_or_create_runbook(
            incident_type=pod["reason"],
            rca_text=rca
        )
        
        rca = generate_rca(
             evidence
       ) 

        result = {
            "cluster": context,
            "namespace": pod["namespace"],
            "pod": pod["pod"],
            "incident_type": pod["reason"],
            "rca": rca,
            "runbook": runbook
        }

        results.append(
            result
        )

    return results