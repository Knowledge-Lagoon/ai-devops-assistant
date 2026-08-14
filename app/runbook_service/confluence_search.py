import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def find_page_by_title(
    title: str
):

    url = f"{CONFLUENCE_URL}/api/v2/pages"

    print("\n=== SEARCH REQUEST ===\n")

    print("URL:", url)
    print("EMAIL:", ATLASSIAN_EMAIL)
    print(
        "TOKEN:",
        "SET" if ATLASSIAN_API_TOKEN else "MISSING"
    )

    response = requests.get(
        url,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        )
    )

    print("\n=== SEARCH RESPONSE ===\n")

    print(
        "Status:",
        response.status_code
    )

    print(
        response.text[:1000]
    )

    response.raise_for_status()

    data = response.json()

    for page in data.get(
        "results",
        []
    ):

        if (
            page["title"].lower()
            == title.lower()
        ):

            return {
                "id": page["id"],
                "title": page["title"],
                "parent": page.get(
                    "parentId"
                )
            }

    return None


if __name__ == "__main__":

    result = find_page_by_title(
        "CrashLoopBackOff"
    )

    print(result)