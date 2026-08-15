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
            f"Cluster context '{context}' not found"
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

                reason