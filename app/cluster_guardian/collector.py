import json
import subprocess

from datetime import datetime


SEVERITY_HINTS = {
    "CrashLoopBackOff": "High",
    "OOMKilled": "High",
    "ImagePullBackOff": "Medium",
    "Pending": "Medium"
}


def run_command(
    command: str
):

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        raise Exception(
            f"Command failed:\n"
            f"{command}\n\n"
            f"{result.stderr}"
        )

    return result.stdout.strip()


def validate_context(
    context: str
):

    output = run_command(
        "kubectl config get-contexts -o name"
    )

    contexts = output.splitlines()

    if context not in contexts:

        raise Exception(
            f"Cluster context '{context}' not found.\n\n"
            f"Available contexts:\n"
            f"{chr(10).join(contexts)}"
        )


def get_failed_pods(
    context: str
):

    validate_context(
        context
    )

    output = run_command(
        f"kubectl --context {context} "
        f"get pods -A -o json"
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

                reason = waiting.get(
                    "reason"
                )

                failed_pods.append(
                    {
                        "cluster": context,
                        "namespace": namespace,
                        "pod": pod_name,
                        "container": status.get(
                            "name"
                        ),
                        "reason": reason,
                        "message": waiting.get(
                            "message"
                        ),
                        "node": item.get(
                            "spec",
                            {}
                        ).get(
                            "nodeName"
                        ),
                        "phase": item.get(
                            "status",
                            {}
                        ).get(
                            "phase"
                        ),
                        "severity_hint": (
                            SEVERITY_HINTS.get(
                                reason,
                                "Unknown"
                            )
                        )
                    }
                )

    return failed_pods


def collect_evidence(
    context: str,
    namespace: str,
    pod: str
):

    validate_context(
        context
    )

    describe_output = run_command(
        f"kubectl --context {context} "
        f"describe pod {pod} "
        f"-n {namespace}"
    )

    logs_output = run_command(
        f"kubectl --context {context} "
        f"logs {pod} "
        f"-n {namespace} "
        f"--tail=100"
    )

    try:

        previous_logs_output = run_command(
            f"kubectl --context {context} "
            f"logs {pod} "
            f"-n {namespace} "
            f"--previous "
            f"--tail=100"
        )

    except Exception:

        previous_logs_output = ""

    events_output = run_command(
        f"kubectl --context {context} "
        f"get events "
        f"-n {namespace} "
        f"--sort-by=.metadata.creationTimestamp"
    )

    deployment_output = run_command(
        f"kubectl --context {context} "
        f"get deployment "
        f"-n {namespace}"
    )

    return {
        "timestamp": (
            datetime.utcnow()
            .isoformat()
        ),
        "cluster": context,
        "namespace": namespace,
        "pod": pod,
        "describe": describe_output,
        "logs": logs_output,
        "previous_logs": previous_logs_output,
        "events": events_output,
        "deployments": deployment_output
    }