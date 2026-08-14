import requests

from app.incident_service.config import (
    JIRA_URL,
    JIRA_USERNAME,
    JIRA_API_TOKEN,
    JIRA_PROJECT_KEY
)


def create_ticket(
    summary: str,
    description: str,
    issue_type: str = "Task"
):

    url = f"{JIRA_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {
                "key": JIRA_PROJECT_KEY
            },
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": issue_type
            }
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=(
            JIRA_USERNAME,
            JIRA_API_TOKEN
        ),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    print("\n=== JIRA RESPONSE ===\n")

    print(
        "Status:",
        response.status_code
    )

    print(
        response.text
    )

    response.raise_for_status()

    data = response.json()

    return {
        "key": data["key"],
        "id": data["id"]
    }


if __name__ == "__main__":

    result = create_ticket(
        summary="[AI Guardian] Test Incident",
        description="""
Platform: Kubernetes

Incident Type: Test Failure

Severity: High

Root Cause:
Testing Jira integration

Runbook:
Confluence Placeholder
"""
    )

    print(result)