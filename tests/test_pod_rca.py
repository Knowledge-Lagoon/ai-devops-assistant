import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app.kubernetes_assistant.cluster_analyzer import get_pod_details, get_pod_logs


class ClusterAnalyzerTests(unittest.TestCase):
    @patch("app.kubernetes_assistant.cluster_analyzer.subprocess.run")
    def test_get_pod_details_includes_kubectl_error_output(self, mock_run):
        mock_run.return_value = SimpleNamespace(
            returncode=1,
            stdout="",
            stderr="Unable to connect to the server",
        )

        result = get_pod_details("crashloop-demo")

        self.assertIn("kubectl command failed", result)
        self.assertIn("Unable to connect to the server", result)

    @patch("app.kubernetes_assistant.cluster_analyzer.subprocess.run")
    def test_get_pod_logs_includes_kubectl_error_output(self, mock_run):
        mock_run.return_value = SimpleNamespace(
            returncode=1,
            stdout="",
            stderr="pod not found",
        )

        result = get_pod_logs("crashloop-demo")

        self.assertIn("kubectl command failed", result)
        self.assertIn("pod not found", result)

    @patch("app.kubernetes_assistant.cluster_analyzer.subprocess.run")
    @patch("app.kubernetes_assistant.cluster_analyzer.KUBECTL_COMMAND", "ssh jumpbox kubectl")
    def test_get_pod_details_uses_kubectl_override_from_environment(self, mock_run):
        mock_run.return_value = SimpleNamespace(
            returncode=0,
            stdout="pod details",
            stderr="",
        )

        result = get_pod_details("crashloop-demo")

        self.assertEqual(result, "pod details")
        self.assertEqual(mock_run.call_args[0][0][0], "ssh")
        self.assertEqual(mock_run.call_args[0][0][1], "jumpbox")
        self.assertEqual(mock_run.call_args[0][0][2], "kubectl")

    @patch("app.kubernetes_assistant.cluster_analyzer.subprocess.run")
    @patch("app.kubernetes_assistant.cluster_analyzer.K8S_NAMESPACE", "custom-ns")
    def test_get_pod_details_uses_namespace_from_environment(self, mock_run):
        mock_run.return_value = SimpleNamespace(
            returncode=0,
            stdout="pod details",
            stderr="",
        )

        get_pod_details("crashloop-demo")

        self.assertEqual(mock_run.call_args[0][0][-2], "-n")
        self.assertEqual(mock_run.call_args[0][0][-1], "custom-ns")


if __name__ == "__main__":
    unittest.main()
