from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.models.weather import WeatherSchema
from app.utils import weather_api_key,weather_api_url
import requests

router = APIRouter()


@router.get("/", response_description="Weather data retrieved")
async def get_weather(city: str, country: str):
    if(len(country) != 2):
        return {"message": "ERROR: Country code must be 2 characters long"}
    city = city.lower()
    country = country.lower()
    try:
        response = requests.get(f'{weather_api_url}?q={city},{country}&appid={weather_api_key}')
        
    except requests.exceptions.RequestException as e:
        return {"message": "ERROR: Could not connect to weather API",
                "description": e}
    return response.json()
