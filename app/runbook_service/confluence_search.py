if __name__ == "__main__":

    pages_to_find = [
        "Kubernetes",
        "CI-CD",
        "Terraform"
    ]

    for page_name in pages_to_find:

        result = find_page_by_title(
            page_name
        )

        print("\n-------------------")

        print(
            f"Searching: {page_name}"
        )

        print(
            result
        )