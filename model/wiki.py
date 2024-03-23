import os
import requests
import json
from bs4 import BeautifulSoup
import html5lib

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
endpoint = "/search/page"
url = base_url + language_code + endpoint
parameters = {"q": search_query, "limit": number_of_results}

print(f"Requesting {url}")

response = requests.get(url, headers=headers, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    data = response.json()
    # Print formatted JSON response
    print(json.dumps(data, indent=4))

    # Process each page in the response
    for page in data["pages"]:
        display_title = page["title"]
        article_url = "https://" + language_code + ".wikipedia.org/wiki/" + page["key"]
        excerpt = page["excerpt"]
        try:
            article_description = page["description"]
        except KeyError:
            article_description = "a Wikipedia article"
        try:
            thumbnail_url = "https:" + page["thumbnail"]["url"]
        except KeyError:
            thumbnail_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png"

        print(f"Title: {display_title}")
        print(f"URL: {article_url}")
        print(f"Description: {article_description}")
        print(f"Excerpt: {excerpt}")
        print(f"Thumbnail URL: {thumbnail_url}\n")

else:
    # Print the error if the request was unsuccessful
    print("Error:", response.status_code, response.text)


r = requests.get(article_url)
soup = BeautifulSoup(
    r.content, "html5lib"
)  # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
