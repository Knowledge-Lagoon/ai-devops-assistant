import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def test_confluence():

    tests = [
        (
            "Space API",
            f"{CONFLUENCE_URL}/rest/api/space"
        ),
        (
            "Search API",
            f"{CONFLUENCE_URL}/rest/api/search"
        ),
        (
            "Content API",
            f"{CONFLUENCE_URL}/rest/api/content"
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
                auth=(
                    ATLASSIAN_EMAIL,
                    ATLASSIAN_API_TOKEN
                )
            )

            print(f"STATUS : {response.status_code}")
            print("BODY:")
            print(response.text[:1000])

        except Exception as ex:

            print(f"ERROR: {ex}")


def search_pages():

    url = f"{CONFLUENCE_URL}/rest/api/search"

    response = requests.get(
        url,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        ),
        params={
            "cql": 'type="page"'
        }
    )

    print("\n" + "=" * 60)
    print("SEARCH TEST")
    print("=" * 60)

    print(f"STATUS : {response.status_code}")
    print(f"URL    : {response.url}")

    if response.status_code != 200:
        print(response.text)
        return

    data = response.json()

    print(f"RESULTS: {data.get('size', 0)}")

    for page in data.get("results", []):

        title = page.get("title")

        page_id = (
            page.get("content", {})
                .get("id")
        )

        print(f"ID={page_id} TITLE={title}")


def get_crashloop_page():

    page_id = "327685"

    url = (
        f"{CONFLUENCE_URL}"
        f"/rest/api/content/{page_id}"
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

    print("\n" + "=" * 60)
    print("PAGE CONTENT TEST")
    print("=" * 60)

    print(f"STATUS : {response.status_code}")
    print(f"URL    : {response.url}")

    if response.status_code != 200:
        print(response.text)
        return

    data = response.json()

    print("SUCCESS")
    print(data["title"])

    body = data["body"]["storage"]["value"]

    print(body[:1000])


if __name__ == "__main__":

    test_confluence()

    search_pages()

    get_crashloop_page()