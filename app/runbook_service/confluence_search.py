import os
from dotenv import load_dotenv

load_dotenv()

print("EMAIL =", os.getenv("ATLASSIAN_EMAIL"))
print("TOKEN LENGTH =", len(os.getenv("ATLASSIAN_API_TOKEN")))
print("CONFLUENCE_URL =", os.getenv("CONFLUENCE_URL"))