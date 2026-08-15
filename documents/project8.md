# Project 8 - AI Cluster Guardian

## Vision

AI Cluster Guardian continuously monitors Kubernetes clusters,
detects failures,
collects evidence,
generates RCA,
searches operational knowledge,
and creates incidents.

---

## Architecture

Monitored Clusters

├── k8s-chaos-lab
├── k8s-chaos-lab-2
└── Future Clusters

        ↓

Cluster Guardian

        ↓

Evidence Collection

- Logs
- Events
- Pod Descriptions
- Deployment Information

        ↓

Incident Analyzer

        ↓

Root Cause Analysis

        ↓

Runbook Service

Search Existing Runbooks

Found?
├── Reuse Existing Runbook
└── Generate New Runbook

        ↓

Confluence

Operational Knowledge Base

        ↓

Incident Service

        ↓

Jira

Incident Tracking