RUNBOOK_GENERATION_PROMPT = """
You are a Senior Site Reliability Engineer.

Generate an operational runbook from the RCA report.

Output sections:

Runbook Title

Symptoms

Business Impact

Root Cause

Resolution Steps

Validation Checks

Escalation Path

References

RCA Report:

{rca}
"""
``