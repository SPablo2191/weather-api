from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.models.weather import WeatherSchema
from app.utils import weather_api_key, weather_api_url,kelvin_to_celsius,kelvin_to_fahrenheit
import requests

router = APIRouter()


@router.get("/", response_description="Weather data retrieved")
async def get_weather(city: str, country: str):
    if len(country) != 2:
        return {"message": "ERROR: Country code must be 2 characters long"}
    city = city.lower()
    country = country.lower()
    data: WeatherSchema = WeatherSchema()
    try:
        response = requests.get(
            f"{weather_api_url}?q={city},{country}&appid={weather_api_key}"
        )
        data.location_name = f"{response.json()['name']}, {response.json()['sys']['country']}"
        fahrenheit_temp = kelvin_to_fahrenheit(response.json()["main"]["temp"])
        celsius_temp = kelvin_to_celsius(response.json()["main"]["temp"])
        data.temperature = (fahrenheit_temp,celsius_temp)
        data.cloudiness = response.json()["weather"][0]["description"]
        data.pressure = response.json()["main"]["pressure"]
        data.humidity = response.json()["main"]["humidity"]
        data.wind = response.json()["wind"]["speed"]
        data.geo_coordinates = [
            response.json()["coord"]["lon"],
            response.json()["coord"]["lat"],
        ]
        print(response.json()["dt"])
        data.requested_time = response.json()["dt"]
        data.sunrise = response.json()["sys"]["sunrise"]
        data.sunset = response.json()["sys"]["sunset"]
    except requests.exceptions.RequestException as e:
        return {"message": "ERROR: Could not connect to weather API", "description": e}
    return data
