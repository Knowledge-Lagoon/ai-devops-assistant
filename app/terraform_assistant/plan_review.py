import re

from app.rag.chat import ask_with_rag

from app.terraform_assistant.prompts import (
    TERRAFORM_PLAN_REVIEW_PROMPT
)


def detect_plan_risks(plan_text: str) -> list[str]:

    findings = []

    lower_text = plan_text.lower()

    if "0.0.0.0/0" in plan_text:

        findings.append(
            "High risk: Open ingress rule detected with cidr_blocks = [\"0.0.0.0/0\"]."
        )

    match = re.search(
        r"(\d+)\s+to destroy",
        lower_text
    )

    if match:

        destroy_count = int(
            match.group(1)
       )

        if destroy_count > 0:

            findings.append(
                f"Potential destructive change detected. "
                f"{destroy_count} resource(s) will be destroyed."
           )

    if "aws_db_instance" in lower_text and "destroy" in lower_text:

        findings.append(
            "Critical risk: Database resource destruction detected."
        )

    if "aws_security_group" in lower_text:

        findings.append(
            "Security group change detected. Review ingress and egress rules carefully."
        )

    if "aws_iam_policy" in lower_text or "aws_iam_role" in lower_text:

        findings.append(
            "IAM change detected. Review permissions for least privilege."
        )

    if not findings:

        findings.append(
            "No high-risk deterministic findings detected."
        )

    return findings


def analyze_plan(plan_text: str) -> str:

    detected_findings = detect_plan_risks(
        plan_text
    )

    detected_findings_text = "\n".join(
        f"- {finding}"
        for finding in detected_findings
    )

    enriched_plan = f"""
Detected Terraform Plan Findings:

{detected_findings_text}

Terraform Plan Output:

{plan_text}
"""

    prompt = TERRAFORM_PLAN_REVIEW_PROMPT.format(
        plan=enriched_plan
    )

    return ask_with_rag(
        prompt,
        retrieval_query=plan_text
   )


if __name__ == "__main__":

    plan_file = input(
        "Enter Terraform plan file: "
    ).strip()

    with open(
        plan_file,
        "r"
    ) as f:

        plan_text = f.read()

    print(
        analyze_plan(
            plan_text
        )
    )