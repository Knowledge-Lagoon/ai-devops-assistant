from app.runbook_service.confluence_search import (
    find_page_by_title
)

from app.runbook_service.confluence_publish import (
    create_runbook_page
)

from app.runbook_service.generator import (
    generate_runbook
)


def get_or_create_runbook(
    incident_type: str,
    rca_text: str
):

    existing_page = find_page_by_title(
        incident_type
    )

    if existing_page:

        page_url = (
            "https://knowledge-lagoon.atlassian.net/wiki/"
            f"spaces/IS/pages/"
            f"{existing_page['id']}/"
            f"{existing_page['title']}"
        )

        print(
            "\n=== EXISTING RUNBOOK FOUND ===\n"
        )

        print(
            page_url
        )

        return {
            "status": "existing",
            "url": page_url
        }

    print(
        "\n=== GENERATING RUNBOOK ===\n"
    )

    runbook = generate_runbook(
        rca_text
    )

    page = create_runbook_page(
        title=incident_type,
        content=runbook
    )

    page_url = (
        "https://knowledge-lagoon.atlassian.net/wiki/"
        f"spaces/IS/pages/"
        f"{page['id']}/"
        f"{page['title']}"
    )

    print(
        "\n=== NEW RUNBOOK CREATED ===\n"
    )

    print(
        page_url
    )

    return {
        "status": "created",
        "url": page_url
    }