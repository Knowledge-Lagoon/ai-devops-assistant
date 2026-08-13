"""
Confluence Runbook Registry

Maps categories to Confluence parent page IDs.
"""

PARENT_PAGES = {
    "kubernetes": {
        "title": "Kubernetes",
        "page_id": None
    },
    "cicd": {
        "title": "CI-CD",
        "page_id": None
    },
    "terraform": {
        "title": "Terraform",
        "page_id": None
    }
}


def get_parent_page(
    category: str
):

    return PARENT_PAGES.get(
        category.lower()
    )