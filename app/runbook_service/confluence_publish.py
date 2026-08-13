import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    CONFLUENCE_SPACE,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def create_page(
    title: str,
    parent_id: str,
    content: str
):

    url = f"{CONFLUENCE_URL}/api/v2/pages"

    payload = {
        "spaceId": CONFLUENCE_SPACE,
        "status": "current",
        "title": title,
        "parentId": parent_id,
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

    print("Status:", response.status_code)
    print(response.text)

    return response

if __name__ == "__main__":

    create_page(
        title="OOMKilled",
        parent_id="262618",
        content="""
Incident Type: OOMKilled

Symptoms:
Container terminated due to memory limits.

Resolution:
Increase memory limits.
Review application memory usage.
"""
    )    