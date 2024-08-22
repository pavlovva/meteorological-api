import os
from typing import Dict

from fastapi import FastAPI, HTTPException

from meteorological_api.services.file_reader import get_data_at_coords

app = FastAPI()

DATA_DIR = os.path.join(os.path.dirname(__file__), '../files')


@app.get("/getForecast", response_model=Dict[int, Dict[str, float]])
async def get_forecast(from_ts: int, to_ts: int, lat: float, lon: float):
    result = {}
    try:
        for ts in range(from_ts, to_ts + 1, 3600):
            file_name = f"{ts}.wgf4"
            file_path = os.path.join(DATA_DIR, file_name)

            if not os.path.exists(file_path):
                raise HTTPException(status_code=404, detail=f"Data file for timestamp {ts} not found.")

            data_value = get_data_at_coords(file_path, lat, lon)
            result[ts] = {"temp": data_value}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
