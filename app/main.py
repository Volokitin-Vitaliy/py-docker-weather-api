import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": AQI
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    get_weather()
