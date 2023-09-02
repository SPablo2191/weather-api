from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.models.weather import WeatherSchema

router = APIRouter()

@router.get("/", response_description="Weather data retrieved")
async def get_weather(city : str, country : str):
    return {"message": f"Hello {city} {country}"}