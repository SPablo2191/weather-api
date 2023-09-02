from fastapi import FastAPI
from app.routes.weather import router as WeatherRouter
from app.utils import EndpointName,weather_api_url
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix=EndpointName.weather)

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "https://weather-api-vgb9.onrender.com",
#     weather_api_url
# ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def index():
    return {"message": "Welcome to the weather API!⛈️"}
