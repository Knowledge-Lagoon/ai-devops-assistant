import os
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_URL = os.getenv(
    "CONFLUENCE_URL"
)

CONFLUENCE_SPACE = os.getenv(
    "CONFLUENCE_SPACE"
)

ATLASSIAN_EMAIL = os.getenv(
    "CONFLUENCE_USERNAME"
)

ATLASSIAN_API_TOKEN = os.getenv(
    "CONFLUENCE_API_TOKEN"
)