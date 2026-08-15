from app.cluster_guardian.service import (
    process_cluster
)

CLUSTER_CONTEXT = (
    "cloud_user@k8s-chaos-lab.us-east-1.eksctl.io"
)

process_cluster(
    CLUSTER_CONTEXT
)