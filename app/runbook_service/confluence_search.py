import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def test_confluence():
    tests = [
        (
            "Space API (v2)",
            f"{CONFLUENCE_URL}/api/v2/spaces"
        ),
        (
            "Pages API (v2)",
            f"{CONFLUENCE_URL}/api/v2/pages"
        )
    ]

    for name, url in tests:
        print("\n" + "=" * 60)
        print(f"TEST : {name}")
        print(f"URL  : {url}")
        print("=" * 60)

        try:
            response = requests.get(
                url,
                auth=(ATLASSIAN_EMAIL, ATLASSIAN_API_TOKEN)
            )

            print(f"STATUS : {response.status_code}")
            print("BODY:")
            print(response.text[:1000])

        except Exception as ex:
            print(f"ERROR: {ex}")


def search_pages():
    # If using modern v2, you filter pages by title or container rather than raw CQL
    url = f"{CONFLUENCE_URL}/api/v2/pages"

    response = requests.get(
        url,
        auth=(ATLASSIAN_EMAIL, ATLASSIAN_API_TOKEN),
        params={
            "limit": 10  # Retrieves the first 10 pages
        }
    )

    print("\n" + "=" * 60)
    print("PAGES LIST TEST (v2)")
    print("=" * 60)

    print(f"STATUS : {response.status_code}")
    print(f"URL    : {response.url}")

    if response.status_code != 200:
        print(response.text)
        return

    data = response.json()
    results = data.get("results", [])
    print(f"RESULTS: {len(results)}")

    for page in results:
        title = page.get("title")
        page_id = page.get("id")
        print(f"ID={page_id} TITLE={title}")


def get_crashloop_page():
    page_id = "327685"

    # Updated to Confluence v2 Endpoint
    url = f"{CONFLUENCE_URL}/api/v2/pages/{page_id}"

    response = requests.get(
        url,
        auth=(ATLASSIAN_EMAIL, ATLASSIAN_API_TOKEN),
        params={
            "body-format": "storage"  # Modern replacement for expand=body.storage
        }
    )

    print("\n" + "=" * 60)
    print("PAGE CONTENT TEST (v2)")
    print("=" * 60)

    print(f"STATUS : {response.status_code}")
    print(f"URL    : {response.url}")

    if response.status_code != 200:
        print(response.text)
        return

    data = response.json()

    print("SUCCESS")
    print(f"Title: {data.get('title')}")

    # Access the body safely via the new JSON path
    body_data = data.get("body", {}).get("storage", {})
    body = body_data.get("value", "No storage body found")

    print(body[:1000])


if __name__ == "__main__":
    test_confluence()
    search_pages()
    get_crashloop_page()