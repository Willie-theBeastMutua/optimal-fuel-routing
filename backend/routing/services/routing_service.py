import os
from dotenv import load_dotenv
import requests

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

def get_route(start, end):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "coordinates": [
            [start["lng"], start["lat"]],
            [end["lng"], end["lat"]]
        ]
    }

    res = requests.post(url, json=payload, headers=headers)
    res.raise_for_status()
    return res.json()

