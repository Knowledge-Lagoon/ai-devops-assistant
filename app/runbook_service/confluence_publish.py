import json
import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    CONFLUENCE_SPACE_ID,
    DEVOPS_RUNBOOKS_PAGE_ID,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def create_runbook_page(
    title: str,
    content: str
):

    print("\n=== CREATE PAGE REQUEST ===\n")

    print(
        "Title:",
        title
    )

    print(
        "Space ID:",
        CONFLUENCE_SPACE_ID
    )

    url = f"{CONFLUENCE_URL}/api/v2/pages"

    payload = {
    "spaceId": CONFLUENCE_SPACE_ID,
    "status": "current",
    "title": title,
    "parentId": DEVOPS_RUNBOOKS_PAGE_ID,
    "body": {
        "representation": "storage",
        "value": f"""
<h1>{title}</h1>
<pre>{content}</pre>
"""
    }
}

    response = requests.post(
        url,
        json=payload,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        ),
        headers={
            "Content-Type": "application/json"
        }
    )

    print(
        "\n=== HTTP RESPONSE ===\n"
    )

    print(
        "Status:",
        response.status_code
    )

    response.raise_for_status()

    data = response.json()

    print(
        "\n=== CONFLUENCE RESPONSE ===\n"
    )

    print(
        json.dumps(
            data,
            indent=2
        )
    )

    return {
        "id": data["id"],
        "title": data["title"]
    }


if __name__ == "__main__":

        create_runbook_page(
        title="TestRunbook999",
        content="""
Incident Type: TestRunbook999

Symptoms:
Test symptoms

Root Cause:
Test root cause

Resolution:
Test resolution
"""
        )
 