from fastapi import FastAPI
from app.routes.weather import router as WeatherRouter
from app.utils import EndpointName

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix=EndpointName.weather)


@app.get("/", tags=["Root"])
async def index():
    return {"message": "Welcome to the weather API!⛈️"}