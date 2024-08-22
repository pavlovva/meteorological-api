import array

import aiofiles
from aiocache import cached, SimpleMemoryCache


async def read_header(file_path: str) -> dict[str, any]:
    async with aiofiles.open(file_path, 'rb') as f:
        header_data = await f.read(28)
        header = array.array('i')
        header.frombytes(header_data)

        latitude1, latitude2, longitude1, longitude2, dx, dy, multiplier = header

        delimiter_data = await f.read(4)
        delimiter = array.array('f')
        delimiter.frombytes(delimiter_data)

        if delimiter[0] != -100500.0:
            raise ValueError("Invalid file format or incorrect delimiter.")

        return {
            "latitude1": latitude1,
            "latitude2": latitude2,
            "longitude1": longitude1,
            "longitude2": longitude2,
            "dx": dx,
            "dy": dy,
            "multiplier": multiplier
        }


@cached(ttl=120, cache=SimpleMemoryCache)
async def get_data_at_coords(file_path: str, lat: float, lon: float) -> float:
    header = await read_header(file_path)

    lat_idx = int((lat * header['multiplier'] - header['latitude1']) / header['dy'])
    lon_idx = int((lon * header['multiplier'] - header['longitude1']) / header['dx'])

    data_index = lat_idx * ((header['longitude2'] - header['longitude1']) // header['dx']) + lon_idx

    async with aiofiles.open(file_path, 'rb') as f:
        await f.seek(8 * 4 + 4)
        await f.seek(data_index * 4, 1)
        data_value_data = await f.read(4)
        data_value = array.array('f')
        data_value.frombytes(data_value_data)

    return data_value[0]
