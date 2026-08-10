# Kubernetes Assistant Module

## Overview

The `kubernetes_assistant` module is designed to assist with Kubernetes cluster management and troubleshooting. It provides tools for analyzing Kubernetes configurations, detecting potential issues, and offering recommendations for best practices.

## Features

1. **Configuration Analysis**:
   - Analyzes Kubernetes manifests (YAML files) for potential misconfigurations.
   - Detects common issues such as:
     - Missing resource limits/requests.
     - Deprecated API versions.
     - Security vulnerabilities in configurations.

2. **Cluster Troubleshooting**:
   - Provides insights into cluster health and resource usage.
   - Detects issues such as:
     - Pod failures.
     - Node resource exhaustion.
     - Misbehaving workloads.

3. **Integration with RAG**:
   - Uses the Retrieval-Augmented Generation (RAG) pipeline to provide context-aware recommendations.
   - Leverages the `ask_with_rag` function to query the knowledge base for Kubernetes best practices.

## Key Components

### `config_analyzer.py`
- **Purpose**: Analyzes Kubernetes configuration files.
- **Functions**:
  - `analyze_manifest(manifest: str) -> list[str]`: Detects issues in a Kubernetes manifest and provides recommendations.

### `cluster_diagnostics.py`
- **Purpose**: Diagnoses issues in a running Kubernetes cluster.
- **Functions**:
  - `check_cluster_health() -> dict`: Provides an overview of cluster health and resource usage.
  - `troubleshoot_pod(pod_name: str) -> str`: Analyzes a specific pod for issues and suggests fixes.

### `prompts.py`
- **Purpose**: Contains the prompt template for Kubernetes-related queries.
- **Key Prompt**:
  - `KUBERNETES_PROMPT`: Defines the structure and rules for generating Kubernetes recommendations.

## Usage

1. **Configuration Analysis**:
   - Use `analyze_manifest` to analyze Kubernetes YAML files for potential issues.
   - Example:
     ```python
     from app.kubernetes_assistant.config_analyzer import analyze_manifest
     manifest = """
     apiVersion: v1
     kind: Pod
     metadata:
       name: example
     spec:
       containers:
       - name: app
         image: nginx
     """
     issues = analyze_manifest(manifest)
     print(issues)
     ```

2. **Cluster Troubleshooting**:
   - Use `check_cluster_health` to get an overview of cluster health.
   - Example:
     ```python
     from app.kubernetes_assistant.cluster_diagnostics import check_cluster_health
     health_report = check_cluster_health()
     print(health_report)
     ```

   - Use `troubleshoot_pod` to analyze a specific pod.
     ```python
     from app.kubernetes_assistant.cluster_diagnostics import troubleshoot_pod
     pod_report = troubleshoot_pod("example-pod")
     print(pod_report)
     ```

## Dependencies

- `app.rag.chat`: Provides the `ask_with_rag` function for querying the knowledge base.
- `kubernetes` Python client: Used for interacting with the Kubernetes API.

## Example Workflow

1. Analyze Kubernetes manifests using `config_analyzer.py` to detect misconfigurations.
2. Diagnose cluster issues using `cluster_diagnostics.py` to identify and resolve problems.
3. Use the RAG pipeline to get context-aware recommendations for Kubernetes best practices.

## Future Enhancements

- Add support for Helm chart analysis.
- Integrate with Prometheus and Grafana for real-time monitoring.
- Enhance troubleshooting with AI-based anomaly detection.

## Example Usage

Run the Kubernetes assistant:
```bash
python -m app.kubernetes_assistant.assistant