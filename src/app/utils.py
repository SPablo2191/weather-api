from dotenv import load_dotenv
from enum import Enum
import os

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
weather_api_url = os.getenv("WEATHER_API_URL")


class EndpointName(str, Enum):
    weather = "/api/weather"




def kelvin_to_celsius(kelvin: float) -> str:
    celsius = kelvin - 273.15
    return f"{round(celsius, 2)} °C"

def kelvin_to_fahrenheit(kelvin: float) -> str:
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return f"{round(fahrenheit, 2)} °F"