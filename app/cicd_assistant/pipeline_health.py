from app.cicd_assistant.pipeline_discovery import (
    discover_pipelines
)

from app.cicd_assistant.analyzer import (
    analyze_pipeline
)


def pipeline_health():

    pipelines = discover_pipelines()

    print("\n=== CI/CD HEALTH REPORT ===\n")

    for pipeline in pipelines:

        print(
            f"Platform: {pipeline['type']}"
        )

        print(
            f"Pipeline: {pipeline['path']}"
        )

        print("\nAnalyzing...\n")

        with open(
            pipeline["path"],
            "r"
        ) as f:

            content = f.read()

        try:
            report = analyze_pipeline(
                content
            )

            print(report)
        except Exception as e:
            print(
                f"Failed to analyze: {e}"
            )

        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":

    pipeline_health()
