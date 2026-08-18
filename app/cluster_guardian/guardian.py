import time

from app.cluster_guardian.cluster_registry import (
    CLUSTERS
)

from app.cluster_guardian.service import (
    process_cluster
)

CHECK_INTERVAL = 300  # 5 minutes


def run():

    print(
        "\n=== AI CLUSTER GUARDIAN STARTED ===\n"
    )

    while True:

        for cluster in CLUSTERS:

            try:

                print(
                    f"\nMonitoring: "
                    f"{cluster['name']}"
                )

                process_cluster(
                    cluster["context"]
                )

            except Exception as ex:

                print(
                    f"\nError processing "
                    f"{cluster['name']}: "
                    f"{ex}"
                )

        print(
            f"\nSleeping for "
            f"{CHECK_INTERVAL} seconds...\n"
        )

        time.sleep(
            CHECK_INTERVAL
        )


if __name__ == "__main__":

    run()