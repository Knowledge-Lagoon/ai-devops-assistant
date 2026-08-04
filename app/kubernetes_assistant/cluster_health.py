import subprocess

from app.kubernetes_assistant.pod_rca import analyze_pod

UNHEALTHY_STATUSES = [
    "CrashLoopBackOff",
    "ImagePullBackOff",
    "ErrImagePull",
    "OOMKilled",
    "Error",
]


def get_unhealthy_pods(namespace="chaos-lab"):

    result = subprocess.run(
        [
            "kubectl",
            "get",
            "pods",
            "-n",
            namespace,
            "--no-headers"
        ],
        capture_output=True,
        text=True
    )

    unhealthy_pods = []

    for line in result.stdout.splitlines():

        parts = line.split()

        if len(parts) < 3:
            continue

        pod_name = parts[0]
        status = parts[2]

        if status in UNHEALTHY_STATUSES:

            unhealthy_pods.append(
                {
                    "pod": pod_name,
                    "status": status
                }
            )

    return unhealthy_pods


def print_cluster_health():

    pods = get_unhealthy_pods()

    print("\n=== CLUSTER HEALTH REPORT ===\n")

    if not pods:

        print("No unhealthy pods detected.")
        return

    for pod in pods:
        print(
            f"Pod: {pod['pod']}"
        )

        print(
            f"Status: {pod['status']}"
        )

        print("\nGenerating RCA...\n")

        try:
            report = analyze_pod(
                pod["pod"],
                "chaos-lab"
            )

            print(report)

        except Exception as e:
            print(
                f"Failed to analyze pod: {e}"
            )

        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":

    print_cluster_health()