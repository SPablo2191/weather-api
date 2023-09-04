import pytest
from fastapi.testclient import TestClient
from app.app import app
from app.utils import cache  
from pytest_mock import mocker 

city = "Bogota"
country = "CO"
fake_city = "Fake City"

@pytest.fixture
def client():
    return TestClient(app)

def test_get_weather(client, mocker):
    response = client.get(f"/api/weather?city={city}&country={country}")
    assert response.status_code == 200
    assert "location_name" in response.json()
    assert "temperature" in response.json()

def test_fake_city(client, mocker):
    response = client.get(f"/api/weather?city={fake_city}&country={country}")
    assert response.status_code == 404


def test_get_weather_with_cached_data(client, mocker):
    cached_data = {
        "location_name": "Bogota, CO",
        "temperature": {"fahrenheit": 72.5, "celsius": 22.5},
    }
    mocker.patch.object(cache, "get", return_value=cached_data)

    response = client.get(f"/api/weather?city={city}&country={country}")

    assert response.status_code == 200
    assert response.json() == cached_data

