import os
import requests


def get_weather():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris&aqi=no"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to get weather data: {response.text}")

    data = response.json()
    city = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Weather in {city}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
