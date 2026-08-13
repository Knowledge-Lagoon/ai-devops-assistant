import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    CONFLUENCE_SPACE_ID,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def create_runbook_page(
    title: str,
    content: str
):
    print(
        "Space ID:",
        CONFLUENCE_SPACE_ID
    )

    url = f"{CONFLUENCE_URL}/api/v2/pages"
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

    response.raise_for_status()

    data = response.json()

    return {
        "id": data["id"],
        "title": data["title"]
    }