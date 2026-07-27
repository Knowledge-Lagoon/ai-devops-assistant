# AKS Notes for DevOps Assistant

## Purpose
Azure Kubernetes Service, commonly called AKS, is a managed Kubernetes service on Azure. Use this document as a starter reference for AKS-related DevOps questions.

## Common areas to document for your environment

- AKS cluster name
- Resource group
- Subscription
- Node pool configuration
- Networking model
- Ingress controller
- Container registry integration
- Monitoring and logging setup
- Backup and disaster recovery approach

## Example operational checks

```bash
az aks get-credentials --resource-group <resource-group> --name <aks-cluster-name>
kubectl get nodes
kubectl get pods -A
```

## Production RAG recommendation
Add your internal AKS architecture diagrams, Terraform module documentation, runbooks, support model, escalation path, and standard operating procedures.

## RAG metadata

- technology: kubernetes
- topic: aks
- doc_type: platform-notes
- source_type: curated-starter
