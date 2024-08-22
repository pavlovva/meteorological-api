import os

import pytest

from meteorological_api.services.file_reader import read_header, get_data_at_coords

FILE = os.path.join(os.path.dirname(__file__), '../../files/1688497200.wgf4')


@pytest.mark.asyncio
async def test_read_header():
    header = await read_header(FILE)
    assert "latitude1" in header
    assert "latitude2" in header
    assert "longitude1" in header
    assert "longitude2" in header
    assert header["multiplier"] > 0


@pytest.mark.asyncio
async def test_get_data_at_coords():
    lat, lon = 50.0, 20.0
    data_value = await get_data_at_coords(FILE, lat, lon)
    assert isinstance(data_value, float)
    assert data_value != -100500.0
