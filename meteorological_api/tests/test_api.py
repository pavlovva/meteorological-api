import pytest
from httpx import AsyncClient, ASGITransport

from meteorological_api.main import app


@pytest.mark.asyncio
async def test_get_forecast():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/getForecast?from_ts=1688504400&to_ts=1688504400&lat=50.0&lon=20.0")
        assert response.status_code == 200
        json_response = response.json()
        assert "1688504400" in json_response
        assert isinstance(json_response["1688504400"]["temp"], float)
