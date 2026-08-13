import os
import requests
from dotenv import load_dotenv

load_dotenv()

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL")
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

print("\n=== DEBUG ===")
print(f"CONFLUENCE_URL       : {CONFLUENCE_URL}")
print(f"USERNAME             : {CONFLUENCE_USERNAME}")
print(f"TOKEN PRESENT        : {bool(CONFLUENCE_API_TOKEN)}")
print("================\n")

url = f"{CONFLUENCE_URL}/rest/api/search"

print(f"Calling URL: {url}")

response = requests.get(
    url,
    auth=(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN),
    params={
        "cql": 'type="page"'
    }
)

print("\n=== RESPONSE ===")
print(f"Status Code : {response.status_code}")
print(f"Request URL : {response.url}")
print(f"Headers     : {response.headers}")
print("Body:")
print(response.text)
print("================\n")
