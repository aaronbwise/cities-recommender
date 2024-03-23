import os
import requests
import json

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

APP_NAME = "Cities Recommender"
EMAIL = "aaronbwise@gmail.com"

language_code = "en"
search_query = "Gainesville, FL"
number_of_results = 1

# Headers for the request
headers = {
    "User-Agent": f"{APP_NAME} ({EMAIL})",
}

base_url = "https://api.wikimedia.org/core/v1/wikipedia/"
endpoint = "search/page"
url = base_url + language_code + "/" + endpoint
parameters = {"q": search_query, "limit": number_of_results}

print(f"Requesting {url}")

response = requests.get(url, headers=headers, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    data = response.json()
    # Print formatted JSON response
    print(json.dumps(data, indent=4))
    # Access and print excerpt
    if "pages" in data and len(data["pages"]) > 0:
        print(data["pages"][0]["excerpt"])
    else:
        print("No pages found in the response.")
else:
    # Print the error if the request was unsuccessful
    print("Error:", response.status_code, response.text)
