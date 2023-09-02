from dotenv import load_dotenv
from enum import Enum
import os
import datetime

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
weather_api_url = os.getenv("WEATHER_API_URL")


class EndpointName(str, Enum):
    weather = "/api/weather"

class ErrorCode(str, Enum):
    correct_request = 200
    bad_request = 400
    not_found = 404
    internal_server_error = 500




def kelvin_to_celsius(kelvin: float) -> str:
    celsius = kelvin - 273.15
    return f"{round(celsius, 2)} °C"

def kelvin_to_fahrenheit(kelvin: float) -> str:
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return f"{round(fahrenheit, 2)} °F"

def get_date(dt_in_seconds: float, timezone_offset_seconds : float, date_format : str) -> datetime:
    return datetime.datetime.fromtimestamp(dt_in_seconds + timezone_offset_seconds).strftime(date_format)
