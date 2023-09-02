from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.models.weather import WeatherSchema
from app.utils import weather_api_key,weather_api_url
import requests

router = APIRouter()


@router.get("/", response_description="Weather data retrieved")
async def get_weather(city: str, country: str):
    response = requests.get(f'{weather_api_url}?q={city},{country}&appid={weather_api_key}')
    return response.json()
