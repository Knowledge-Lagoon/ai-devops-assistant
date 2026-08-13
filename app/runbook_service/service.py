from app.runbook_service.confluence_search import (
    find_page_by_title
)

from app.runbook_generator.generator import (
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

        print(
            "\n=== EXISTING RUNBOOK FOUND ===\n"
        )

        print(
            f"Title: {existing_page['title']}"
        )

        print(
            f"Page ID: {existing_page['id']}"
        )

        print(
            f"\nURL:\n"
            f"https://knowledge-lagoon.atlassian.net/wiki/spaces/IS/pages/"
            f"{existing_page['id']}/"
            f"{existing_page['title']}"
        )

        return existing_page

    print(
        "\n=== GENERATING NEW RUNBOOK ===\n"
    )

    runbook = generate_runbook(
        rca_text
    )

    print(runbook)

    return runbook