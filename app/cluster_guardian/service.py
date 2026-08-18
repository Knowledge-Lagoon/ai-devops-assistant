import time

from app.cluster_guardian.collector import (
    get_failed_pods,
    collect_evidence
)

from app.cluster_guardian.analyzer import (
    generate_rca
)

from app.cluster_guardian.state import (
    incident_exists,
    register_incident,
    get_ticket_key
)

from app.runbook_service.service import (
    get_or_create_runbook
)

from app.incident_service.jira_client import (
    create_ticket
)


def create_guardian_ticket(
    pod: dict,
    evidence: dict,
    runbook: dict
):

    summary = (
        f"[AI Cluster Guardian] "
        f"{pod['reason']} detected"
    )

    description = f"""
Platform: Kubernetes

Cluster:
{pod['cluster']}

Namespace:
{pod['namespace']}

Pod:
{pod['pod']}

Incident Type:
{pod['reason']}

Severity:
{pod['severity_hint']}

Logs:
{evidence['logs']}

Events:
{evidence['events']}

Runbook:
{runbook.get('url', 'Not Available')}

Detected By:
AI Cluster Guardian
"""

    return create_ticket(
        summary=summary,
        description=description
    )


def process_cluster(
    context: str
):

    print(
        f"\n=== PROCESSING CLUSTER: "
        f"{context} ===\n"
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

        #
        # PHASE 2 OPTIMIZATION
        # Check incident memory FIRST.
        # Don't waste time generating RCA
        # for an incident we already know about.
        #
        if incident_exists(
            pod
        ):

            existing_ticket = (
                get_ticket_key(
                    pod
                )
            )

            print(
                f"\nIncident already exists: "
                f"{existing_ticket}"
            )

            continue

        evidence = collect_evidence(
            context=context,
            namespace=pod["namespace"],
            pod=pod["pod"]
        )

        evidence["incident_type"] = (
            pod["reason"]
        )

        print(
            "Generating RCA"
        )

        start = time.time()

        rca = generate_rca(
            evidence
        )

        print(
            f"RCA completed in "
            f"{time.time() - start:.2f}s"
        )

        print(
            "Searching / Creating Runbook"
        )

        runbook = get_or_create_runbook(
            incident_type=pod["reason"],
            rca_text=rca
        )

        print(
            "\nCreating Jira Ticket"
        )

        ticket = create_guardian_ticket(
            pod=pod,
            evidence=evidence,
            runbook=runbook
        )

        register_incident(
            pod,
            ticket["key"]
        )

        print(
            f"Jira Ticket Created: "
            f"{ticket['key']}"
        )

        result = {
            "cluster": context,
            "namespace": pod["namespace"],
            "pod": pod["pod"],
            "incident_type": pod["reason"],
            "severity": pod["severity_hint"],
            "rca": rca,
            "runbook": runbook,
            "jira_ticket": ticket
        }

        results.append(
            result
        )

    return results