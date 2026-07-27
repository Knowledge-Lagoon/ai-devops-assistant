# Kubernetes Overview

## Purpose
Kubernetes is used to orchestrate containerized workloads. It helps teams deploy, scale, and manage applications across clusters of machines.

## Core concepts

### Cluster
A Kubernetes cluster is made up of a control plane and worker nodes. The control plane manages cluster state and scheduling. Worker nodes run application workloads.

### Pod
A Pod is the smallest deployable unit in Kubernetes. It usually contains one application container, but it can contain multiple tightly coupled containers.

### Deployment
A Deployment manages replicas of Pods and supports rolling updates and rollbacks.

### Service
A Service provides a stable network endpoint for accessing Pods, even when individual Pods are replaced.

### Namespace
Namespaces help logically separate resources within the same cluster.

## Common DevOps questions this document can answer

- What is Kubernetes used for?
- What is the difference between a Pod and a Deployment?
- Why do we need Services in Kubernetes?
- How do namespaces help organize workloads?

## Useful commands

```bash
kubectl get nodes
kubectl get pods -A
kubectl get deployments -A
kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace>
```

## RAG metadata

- technology: kubernetes
- topic: overview
- doc_type: concept
- source_type: curated-starter
