from dotenv import load_doten
import os

load_dotenv()

weather_api_key = os.getenv('WEATHER_API_KEY')
weather_api_url = os.getenv('WEATHER_API_URL')