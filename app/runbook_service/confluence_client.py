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
    "ATLASSIAN_EMAIL"
)

ATLASSIAN_API_TOKEN = os.getenv(
    "ATLASSIAN_API_TOKEN"
)