import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)

page_id = "98328"

url = f"{CONFLUENCE_URL}/api/v2/pages/{page_id}"

response = requests.get(
    url,
    auth=(
        ATLASSIAN_EMAIL,
        ATLASSIAN_API_TOKEN
    )
)

print(response.status_code)
print(response.text)
