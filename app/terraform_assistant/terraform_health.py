from app.terraform_assistant.terraform_discovery import (
    discover_terraform_files
)

from app.terraform_assistant.analyzer import (
    analyze_terraform
)


def calculate_basic_scores(terraform_text: str) -> dict:

    security_score = 100
    reliability_score = 100
    cost_score = 100
    maintainability_score = 100

    lower_text = terraform_text.lower()

    if "0.0.0.0/0" in terraform_text:

        security_score -= 35

    if "from_port   = 22" in terraform_text or "from_port = 22" in terraform_text:

        security_score -= 20

    if "cidr_blocks" in lower_text and "0.0.0.0/0" in terraform_text:

        security_score -= 10

    if "tags" not in lower_text:

        maintainability_score -= 20

    if "required_providers" not in lower_text:

        maintainability_score -= 15

    if "backend" not in lower_text:

        reliability_score -= 15

    if "multi_az" not in lower_text and "availability_zone" not in lower_text:

        reliability_score -= 10

    if "instance_type" in lower_text and (
        "xlarge" in lower_text
        or "2xlarge" in lower_text
        or "4xlarge" in lower_text
        or "8xlarge" in lower_text
    ):

        cost_score -= 25

    scores = {
        "security": max(security_score, 0),
        "reliability": max(reliability_score, 0),
        "cost": max(cost_score, 0),
        "maintainability": max(maintainability_score, 0),
    }

    scores["overall"] = round(
        (
            scores["security"]
            + scores["reliability"]
            + scores["cost"]
            + scores["maintainability"]
        ) / 4
    )

    return scores


def print_score_summary(scores: dict):

    print("Basic Health Scores:")
    print(f"- Overall Health Score: {scores['overall']}/100")
    print(f"- Security Score: {scores['security']}/100")
    print(f"- Reliability Score: {scores['reliability']}/100")
    print(f"- Cost Score: {scores['cost']}/100")
    print(f"- Maintainability Score: {scores['maintainability']}/100")
    print()


def terraform_health():

    files = discover_terraform_files()

    print("\n=== TERRAFORM HEALTH REPORT ===\n")

    if not files:

        print("No Terraform files found under terraform/")
        return

    total_files = len(files)

    portfolio_scores = {
        "overall": 0,
        "security": 0,
        "reliability": 0,
        "cost": 0,
        "maintainability": 0,
    }

    print(f"Total Terraform Files Found: {total_files}\n")

    for file_path in files:

        print("=" * 80)
        print(f"Terraform File: {file_path}")
        print("=" * 80)
        print()

        try:

            with open(
                file_path,
                "r"
            ) as f:

                terraform_text = f.read()

            scores = calculate_basic_scores(
                terraform_text
            )

            for key in portfolio_scores:

                portfolio_scores[key] += scores[key]

            print_score_summary(
                scores
            )

            print("AI Review:")
            print()

            report = analyze_terraform(
                terraform_text
            )

            print(report)

        except Exception as e:

            print(
                f"Failed to analyze {file_path}: {e}"
            )

        print("\n")

    print("=" * 80)
    print("PORTFOLIO SUMMARY")
    print("=" * 80)
    print()

    print(f"Terraform Files Analyzed: {total_files}")

    print(
        f"Average Overall Health Score: "
        f"{round(portfolio_scores['overall'] / total_files)}/100"
    )

    print(
        f"Average Security Score: "
        f"{round(portfolio_scores['security'] / total_files)}/100"
    )

    print(
        f"Average Reliability Score: "
        f"{round(portfolio_scores['reliability'] / total_files)}/100"
    )

    print(
        f"Average Cost Score: "
        f"{round(portfolio_scores['cost'] / total_files)}/100"
    )

    print(
        f"Average Maintainability Score: "
        f"{round(portfolio_scores['maintainability'] / total_files)}/100"
    )


if __name__ == "__main__":

    terraform_health()