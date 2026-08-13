import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)

url = f"{CONFLUENCE_URL}/api/v2/folders"

response = requests.get(
    url,
    auth=(
        ATLASSIAN_EMAIL,
        ATLASSIAN_API_TOKEN
    )
)

print(response.status_code)
print(response.text)