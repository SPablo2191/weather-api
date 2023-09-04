import pytest
from fastapi.testclient import TestClient
from app.app import app
from app.utils import cache  


city = "Bogota"
country = "CO"

@pytest.fixture
def client():
    return TestClient(app)

def test_get_weather_with_cache(client, mocker):
    mocker.patch.object(cache, "get", return_value=None)
    mocker.patch.object(cache, "set", return_value=None)

    response = client.get(f"/weather?city={city}&country={country}")

    assert response.status_code == 200
    assert "location_name" in response.json()
    assert "temperature" in response.json()


def test_get_weather_with_cached_data(client, mocker):
    cached_data = {
        "location_name": "Bogota, CO",
        "temperature": {"fahrenheit": 72.5, "celsius": 22.5},
    }
    mocker.patch.object(cache, "get", return_value=cached_data)

    response = client.get(f"/weather?city={city}&country={country}")

    assert response.status_code == 200
    assert response.json() == cached_data

