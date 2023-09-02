from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.app.models.weather import WeatherSchema

router = APIRouter()
