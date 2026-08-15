from app.incident_service.jira_client import (
    create_ticket
)


result = create_ticket(
    summary="[AI Cluster Guardian] CrashLoopBackOff detected",
    description="""
Platform: Kubernetes

Cluster:
k8s-chaos-lab

Namespace:
chaos-lab

Pod:
crashloop-demo-5495bf69b-4wmmg

Incident Type:
CrashLoopBackOff

Severity:
High

Evidence:
Database connection failed
Unable to connect to postgres-service

Events:
Back-off restarting failed container

Detected By:
AI Cluster Guardian
"""
)

print(result)