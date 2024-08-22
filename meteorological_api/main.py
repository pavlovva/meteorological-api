import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Meteorological API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
