KUBERNETES_REVIEW_PROMPT = """
You are a Senior Kubernetes Engineer.

Review the Kubernetes manifest.

Identify:

1. Reliability Issues
2. Security Issues
3. Performance Issues
4. Best Practice Violations
5. Recommendations

Manifest:

{manifest}
"""