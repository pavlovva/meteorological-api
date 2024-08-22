import array


def read_header(file_path: str) -> dict[str, any]:
    with open(file_path, 'rb') as f:
        header = array.array('i')
        header.fromfile(f, 7)

        latitude1, latitude2, longitude1, longitude2, dx, dy, multiplier = header

        delimiter = array.array('f')
        delimiter.fromfile(f, 1)

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


def get_data_at_coords(file_path: str, lat: float, lon: float) -> float:
    header = read_header(file_path)

    lat_idx = int((lat * header['multiplier'] - header['latitude1']) / header['dy'])
    lon_idx = int((lon * header['multiplier'] - header['longitude1']) / header['dx'])

    data_index = lat_idx * ((header['longitude2'] - header['longitude1']) // header['dx']) + lon_idx

    with open(file_path, 'rb') as f:
        f.seek(8 * 4 + 4)
        f.seek(data_index * 4, 1)
        data_value = array.array('f')
        data_value.fromfile(f, 1)

    return data_value[0]
