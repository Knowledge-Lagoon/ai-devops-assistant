from app.cluster_guardian.cluster_registry import (
    CLUSTERS
)

from app.cluster_guardian.service import (
    process_cluster
)

CONTEXT = CLUSTERS[0]["context"]

print("\n======= FIRST RUN =======\n")

process_cluster(
    CONTEXT
)

print("\n======= SECOND RUN =======\n")

process_cluster(
    CONTEXT
)