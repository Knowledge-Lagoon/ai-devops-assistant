import requests

from app.runbook_service.confluence_client import (
    CONFLUENCE_URL,
    ATLASSIAN_EMAIL,
    ATLASSIAN_API_TOKEN
)


def find_page_by_title(
    title: str
):

    url = (
        f"{CONFLUENCE_URL}/api/v2/pages"
    )

    response = requests.get(
        url,
        auth=(
            ATLASSIAN_EMAIL,
            ATLASSIAN_API_TOKEN
        )
    )

    print(response.status_code)
    print(response.text[:500])


if __name__ == "__main__":

    find_page_by_title(
        "CrashLoopBackOff"
    )