from app.cluster_guardian.service import (
    process_cluster
)

CONTEXT = (
    "your_cluster_context_here"
)

print("\n======= FIRST RUN =======\n")

process_cluster(
    CONTEXT
)

print("\n======= SECOND RUN =======\n")

process_cluster(
    CONTEXT
)