# Kubernetes kubectl Troubleshooting

## Purpose
This document provides common `kubectl` commands for first-level Kubernetes troubleshooting.

## Check cluster access

```bash
kubectl cluster-info
kubectl config current-context
kubectl get nodes
```

## Check workloads

```bash
kubectl get pods -A
kubectl get pods -n <namespace>
kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace>
```

## Common issues

### Pod is Pending
Possible areas to check:
- Node capacity
- Scheduling constraints
- Persistent volume claims
- Taints and tolerations

### Pod is CrashLoopBackOff
Possible areas to check:
- Application logs
- Container command or entrypoint
- Environment variables
- Secrets or ConfigMaps
- Readiness and liveness probes

### ImagePullBackOff
Possible areas to check:
- Image name and tag
- Registry access
- Image pull secret
- Network access to registry

## RAG metadata

- technology: kubernetes
- topic: troubleshooting
- doc_type: runbook
- source_type: curated-starter
