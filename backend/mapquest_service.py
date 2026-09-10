import os
import requests

API_KEY = os.getenv("MAPQUEST_API_KEY")
URL = "https://www.mapquestapi.com/directions/v2/route"


def get_route(origin, destination, unit="m", route_type="fastest"):
    origin = origin.strip()
    destination = destination.strip()

    if not origin or not destination:
        return {
            "success": False,
            "error": "Starting location and destination cannot be empty."
        }

    if not API_KEY:
        return {
            "success": False,
            "error": "MapQuest API key is not set."
        }

    params = {
        "key": API_KEY,
        "from": origin,
        "to": destination,
        "unit": unit,
        "routeType": route_type
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        return {
            "success": False,
            "error": "MapQuest request failed."
        }

    data = response.json()

    if data["info"]["statuscode"] != 0:
        return {
            "success": False,
            "error": "MapQuest could not find a valid route."
        }

    distance = data["route"]["distance"]
    travel_time = data["route"]["formattedTime"]
    maneuvers = data["route"]["legs"][0]["maneuvers"]

    directions = []

    for step in maneuvers:
        directions.append(step["narrative"])

    return {
        "success": True,
        "distance": distance,
        "travel_time": travel_time,
        "unit": unit,
        "route_type": route_type,
        "directions": directions
    }