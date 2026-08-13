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

    print(
        "\n=== CREATE PAGE RESPONSE ===\n"
    )

    print(
        "Status:",
        response.status_code
    )

    print(
        response.text
    )

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    create_runbook_page(
        title="OOMKilled",
        content="""
Incident Type: OOMKilled

Symptoms:
Container terminated due to memory pressure.

Root Cause:
Pod exceeded configured memory limits.

Resolution Steps:
1. Review pod memory usage.
2. Increase memory limits.
3. Tune the application.
"""
    )