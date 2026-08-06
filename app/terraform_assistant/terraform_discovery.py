from pathlib import Path


def discover_terraform_files():

    terraform_files = []

    terraform_dir = Path("terraform")

    if not terraform_dir.exists():

        return terraform_files

    for file in terraform_dir.rglob("*.tf"):

        if file.is_file():

            terraform_files.append(
                str(file)
            )

    return terraform_files