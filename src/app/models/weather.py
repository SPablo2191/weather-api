from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class WeatherSchema(BaseModel):
    location_name: str | None = None
    temperature: str | None = None
    wind: str | None = None
    cloudiness: str | None = None
    pressure: str | None = None
    humidity: str | None = None
    sunrise: str | None = None
    sunset: str | None = None
    geo_coordinates: str | None = None
    requested_time: datetime | None = None
