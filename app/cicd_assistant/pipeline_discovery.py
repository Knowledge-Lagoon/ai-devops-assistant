from pathlib import Path

def discover_pipelines():

    pipelines = []

    ado_dir = Path("pipelines/ado")
    jenkins_dir = Path("pipelines/jenkins")

    if ado_dir.exists():

        for file in ado_dir.glob("*"):

            if file.is_file():

                pipelines.append(
                    {
                        "type": "Azure DevOps",
                        "path": str(file)
                    }
                )

    if jenkins_dir.exists():

        for file in jenkins_dir.glob("*"):

            if file.is_file():

                pipelines.append(
                    {
                        "type": "Jenkins",
                        "path": str(file)
                    }
                )

    return pipelines