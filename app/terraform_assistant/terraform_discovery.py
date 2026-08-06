from pathlib import Path


def discover_terraform_files():

    terraform_files = []

    terraform_dir = Path("terraform")

    if terraform_dir.exists():

        for file in terraform_dir.rglob("*.tf"):

            terraform_files.append(
                str(file)
            )

    return terraform_files