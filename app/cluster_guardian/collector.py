import json
import subprocess


def run_command(
    command: str
):

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


def get_failed_pods():

    output = run_command(
        "kubectl get pods -A -o json"
    )

    data = json.loads(
        output
    )

    failed_pods = []

    for item in data.get(
        "items",
        []
    ):

        namespace = item[
            "metadata"
        ][
            "namespace"
        ]

        pod_name = item[
            "metadata"
        ][
            "name"
        ]

        statuses = item.get(
            "status",
            {}
        ).get(
            "containerStatuses",
            []
        )

        for status in statuses:

            waiting = status.get(
                "state",
                {}
            ).get(
                "waiting"
            )

            if waiting:

                failed_pods.append(
                    {
                        "namespace": namespace,
                        "pod": pod_name,
                        "reason": waiting.get(
                            "reason"
                        )
                    }
                )

    return failed_pods


def collect_evidence(
    namespace: str,
    pod: str
):

    describe_output = run_command(
        f"kubectl describe pod {pod} -n {namespace}"
    )

    logs_output = run_command(
        f"kubectl logs {pod} -n {namespace} --tail=100"
    )

    events_output = run_command(
        f"kubectl get events "
        f"-n {namespace} "
        "--sort-by=.metadata.creationTimestamp"
    )

    return {
        "namespace": namespace,
        "pod": pod,
        "describe": describe_output,
        "logs": logs_output,
        "events": events_output
    }


if __name__ == "__main__":

    failed_pods = get_failed_pods()

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
            pod["namespace"],
            pod["pod"]
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