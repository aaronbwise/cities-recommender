import os
import requests
import json

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")


def get_place_id(place_name):
    """
    Get the PlaceID for a given place name.

    Args:
        place_name (str): The name of the place to search for.

    Returns:
        str: The PlaceID if found, else None.
    """
    url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={place_name}&key={API_KEY}"
    response = requests.get(url)
    response_json = response.json()

    # Extract the first result from the autocomplete suggestions
    place_id = response_json["predictions"][0]["place_id"]
    return place_id


def get_place_details(place_id):
    """
    Get the details of a place given its PlaceID.

    Args:
        place_id (str): The PlaceID of the place to search for.

    Returns:
        dict: A dictionary containing the place details.
    """
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
    response = requests.get(url)
    response_json = response.json()

    # Extract the place details
    place_details = json.dumps(response_json["result"], indent=4)
    return place_details


# Enter the place name you want to search for
place_name = input("Enter the place name: ")

# Get the PlaceID
place_id = get_place_id(place_name)

# Print the PlaceID if it exists
if place_id:
    print(f"PlaceID: {place_id}")
else:
    print(f"No place found with the name '{place_name}'.")

# Get the place details
place_details = get_place_details(place_id)
print(place_details)
