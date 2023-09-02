from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class WeatherSchema(BaseModel):
    location_name: str 
    temperature: str 
    wind: str 
    cloudiness: str 
    pressure: str 
    humidity: str
    sunrise: str 
    sunset: str
    geo_coordinates: str 
    requested_time: datetime 
