import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def find_page_by_title(title: str):

    url = f"{CONFLUENCE_URL}/rest/api/search"

    response = requests.get(
        url,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        ),
        params={
            "cql": f'title="{title}"'
        }
    )

    print("\n=== SEARCH REQUEST ===")
    print(f"URL: {response.url}")
    print(f"STATUS: {response.status_code}")

    if response.status_code != 200:
        print(response.text)
        return None

    data = response.json()

    print(f"RESULTS FOUND: {data.get('size', 0)}")

    if data.get("size", 0) == 0:
        print(f"Page '{title}' not found")
        return None

    page = data["results"][0]

    page_id = page["content"]["id"]

    print("\n=== PAGE FOUND ===")
    print(f"TITLE: {page['title']}")
    print(f"PAGE ID: {page_id}")

    return page_id


def get_page_content(page_id: str):

    url = (
        f"{CONFLUENCE_URL}/rest/api/content/"
        f"{page_id}"
    )

    response = requests.get(
        url,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        ),
        params={
            "expand": "body.storage"
        }
    )

    print("\n=== CONTENT REQUEST ===")
    print(f"URL: {response.url}")
    print(f"STATUS: {response.status_code}")

    if response.status_code != 200:
        print(response.text)
        return None

    data = response.json()

    body = data["body"]["storage"]["value"]

    print("\n==