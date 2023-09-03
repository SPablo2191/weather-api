from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.weather import WeatherSchema
from app.utils import (
    weather_api_key,
    weather_api_url,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    get_date,
    ErrorCode,
    cache,
)
import httpx

router = APIRouter()


def data_temperature(value: float) -> dict:
    fahrenheit_temp = kelvin_to_fahrenheit(value)
    celsius_temp = kelvin_to_celsius(value)
    return {
        "fahrenheit": fahrenheit_temp,
        "celsius": celsius_temp,
    }


@router.get("/", response_description="Weather data retrieved")
async def get_weather(city: str, country: str):
    if len(country) != 2:
        return JSONResponse(
            content={"message": "ERROR: Country code must be 2 characters long"},
            status_code=ErrorCode.bad_request,
        )
    city = city.lower()
    country = country.lower()
    cache_key = f"{city.lower()}-{country.lower()}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JSONResponse(content=cached_data, status_code=ErrorCode.ok_request)
    data: WeatherSchema = WeatherSchema()
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{weather_api_url}?q={city},{country}&appid={weather_api_key}"
            )
            if response.status_code != 200:
                return JSONResponse(
                    content={
                        "message": "ERROR: Weather data not found",
                        "description": response.json(),
                    },
                    status_code=ErrorCode.not_found,
                )
            data.location_name = (
                f"{response.json()['name']}, {response.json()['sys']['country']}"
            )
            data.temperature = data_temperature(response.json()["main"]["temp"])
            data.wind = f"{response.json()['wind']['speed']} m/s"
            data.geo_coordinates = [
                response.json()["coord"]["lon"],
                response.json()["coord"]["lat"],
            ]
            data.cloudiness = str(
                response.json()["weather"][0]["description"]
            ).capitalize()
            data.pressure = f'{response.json()["main"]["pressure"]} hpa'
            data.humidity = f'{response.json()["main"]["humidity"]}%'
            data.requested_time = get_date(
                dt_in_seconds=response.json()["dt"],
                timezone_offset_seconds=response.json()["timezone"],
                date_format="%Y-%m-%d %H:%M:%S",
            )
            data.sunrise = get_date(
                dt_in_seconds=response.json()["sys"]["sunrise"],
                timezone_offset_seconds=response.json()["timezone"],
                date_format="%H:%M",
            )
            data.sunset = data.sunrise = get_date(
                dt_in_seconds=response.json()["sys"]["sunset"],
                timezone_offset_seconds=response.json()["timezone"],
                date_format="%H:%M",
            )
            cache[cache_key] = data.dict()
        except httpx.RequestError as e:
            return JSONResponse(
                content={
                    "message": "ERROR: Could not connect to weather API",
                    "description": str(e),
                },
                status_code=ErrorCode.internal_server_error,
            )
    weather_response = JSONResponse(
        content=data.dict(), status_code=ErrorCode.ok_request
    )
    weather_response.headers["Content-Type"] = "application/json"
    return weather_response
