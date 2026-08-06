from app.terraform_assistant.terraform_discovery import (
    discover_terraform_files
)

from app.terraform_assistant.analyzer import (
    analyze_terraform
)


def terraform_health():

    files = discover_terraform_files()

    print(
        "\n=== TERRAFORM HEALTH REPORT ===\n"
    )

    for file_path in files:

        print(
            f"Terraform File: {file_path}"
        )

        print(
            "\nAnalyzing...\n"
        )

        try:

            with open(
                file_path,
                "r"
            ) as f:

                terraform_text = f.read()

            report = analyze_terraform(
                terraform_text
            )

            print(report)

        except Exception as e:

            print(
                f"Failed: {e}"
            )

        print(
            "\n" + "=" * 80 + "\n"
        )


if __name__ == "__main__":

    terraform_health()