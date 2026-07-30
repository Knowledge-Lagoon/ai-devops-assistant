from app.rag.chat import ask_with_rag

from app.kubernetes_assistant.prompts import (
    KUBERNETES_REVIEW_PROMPT
)


def analyze_manifest(manifest_text: str):

    prompt = KUBERNETES_REVIEW_PROMPT.format(
        manifest=manifest_text
    )

    return ask_with_rag(prompt)

if __name__ == "__main__":

    with open(
        "manifests/deployment.yaml",
        "r"
    ) as f:

        manifest = f.read()

    result = analyze_manifest(
        manifest
    )

    print(result)