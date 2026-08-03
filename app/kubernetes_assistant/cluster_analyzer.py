import subprocess


def get_pod_details(pod_name, namespace="default"):

    result = subprocess.run(
        [
            "kubectl",
            "describe",
            "pod",
            pod_name,
            "-n",
            namespace
        ],
        capture_output=True,
        text=True
    )

    return result.stdout


def get_pod_logs(pod_name, namespace="default"):

    result = subprocess.run(
        [
            "kubectl",
            "logs",
            pod_name,
            "-n",
            namespace,
            "--previous"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout