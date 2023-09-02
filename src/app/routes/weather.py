from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.app.models.weather import WeatherSchema

router = APIRouter()

@router.get("/api/weather", response_description="Weather data retrieved")
async def get_weather(city : str, country : str):
    return {"message": f"Hello {city} {country}"}