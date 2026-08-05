PIPELINE_REVIEW_PROMPT = """
You are a Senior DevOps Engineer.

Review the CI/CD pipeline.

Determine:

1. Missing Stages
2. Security Risks
3. Reliability Risks
4. Best Practice Violations
5. Recommendations

Pipeline:

{pipeline}
"""