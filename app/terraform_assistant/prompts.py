TERRAFORM_REVIEW_PROMPT = """
You are a Senior Cloud and DevOps Architect.

Review the Terraform configuration.

Provide:

1. Security Issues
2. Reliability Issues
3. Cost Optimization Opportunities
4. Best Practice Violations
5. Recommendations

Terraform Configuration:

{terraform}
"""