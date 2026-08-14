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

    print(
        "Parent ID:",
        DEVOPS_RUNBOOKS_PAGE_ID
    )

    url = f"{CONFLUENCE_URL}/api/v2/pages"

    payload = {
        "spaceId": CONFLUENCE_SPACE_ID,
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": f"""
<h1>{title}</h1>
<pre>{content}</pre>
"""
        }
    }

    print(
        "\n=== REQUEST PAYLOAD ===\n"
    )

    print(
        json.dumps(
            payload,
            indent=2
        )
    )

    response = requests.post(
        url,
        json=payload,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        ),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    )

    print(
        "\n=== HTTP RESPONSE ===\n"
    )

    print(
        "Status:",
        response.status_code
    )

    print(
        "\n=== RESPONSE BODY ===\n"
    )

    print(
        response.text
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
        title="PodPending",
        content="""
Incident Type: PodPending

Symptoms:
Pods remain in Pending state.

Root Cause:
Insufficient cluster resources.

Resolution Steps:
1. Check node capacity.
2. Check resource requests.
3. Scale cluster if required.
"""
    )