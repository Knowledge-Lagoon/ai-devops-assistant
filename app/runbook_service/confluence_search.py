import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)

url = f"{CONFLUENCE_URL}/api/v2/pages"

response = requests.get(
    url,
    auth=(
        ATLASSIAN_EMAIL,
        ATLASSIAN_API_TOKEN
    )
)

data = response.json()

for page in data.get("results", []):

    print(
        f"Title: {page['title']}"
    )

    print(
        f"ID: {page['id']}"
    )

    print(
        f"Parent: {page.get('parentId')}"
    )

    print("-" * 50)