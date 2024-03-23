import os
import requests
import json
import datetime

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

APP_NAME = "Cities Recommender"
EMAIL = "(aaronbwise@gmail.com)"

language_code = "en"  # English
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "User-Agent": "{APP_NAME} {EMAIL}",
}

today = datetime.datetime.now()
date = today.strftime("%Y/%m/%d")

base_url = "https://api.wikimedia.org/feed/v1/wikipedia/"
url = base_url + language_code + "/featured/" + date
print(f"Requesting {url}")
response = requests.get(url, headers=headers)

# print(json.dumps(response.json(), indent=4))
