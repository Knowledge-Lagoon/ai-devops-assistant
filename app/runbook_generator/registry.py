from pathlib import Path


def find_runbook_by_incident(
    incident_type: str
):

    runbooks_dir = Path(
        "runbooks"
    )

    if not runbooks_dir.exists():

        return None

    for file in runbooks_dir.rglob(
        "*.md"
    ):

        try:

           content = file.read_text()

           if (
                f"In*ident Type: {incident_type}"
               in content
              ):

                return str(file)
        except Exception:

            pass

    return None