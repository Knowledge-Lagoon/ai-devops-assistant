import os
import shlex
import subprocess


def _build_kubectl_command(*args):
    override = os.getenv("KUBECTL_COMMAND")
    if override:
        parts = shlex.split(override)
        return parts + list(args)
    return ["kubectl"] + list(args)


def _run_kubectl(*args):
    command = _build_kubectl_command(*args)
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        error_output = result.stderr.strip() or result.stdout.strip() or "unknown kubectl error"
        return f"kubectl command failed: {error_output}"

    return result.stdout


def get_pod_details(pod_name, namespace="default"):
    return _run_kubectl("describe", "pod", pod_name, "-n", namespace)


def get_pod_logs(pod_name, namespace="default"):
    return _run_kubectl("logs", pod_name, "-n", namespace, "--previous")