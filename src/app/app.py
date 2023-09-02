from fastapi import FastAPI
from app.routes.weather import router as WeatherRouter

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix="/api/weather")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the weather API!⛈️"}