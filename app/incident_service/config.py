import os
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv(
    "JIRA_URL"
)

JIRA_USERNAME = os.getenv(
    "JIRA_USERNAME"
)

JIRA_API_TOKEN = os.getenv(
    "JIRA_API_TOKEN"
)

JIRA_PROJECT_KEY = os.getenv(
    "JIRA_PROJECT_KEY"
)