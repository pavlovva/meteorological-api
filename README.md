
# Meteorological API

Meteorological API is a FastAPI-based service that provides meteorological data by reading from binary files. The service allows users to query temperature data based on geographical coordinates and time intervals.

## Features

- **GET /getForecast:** Fetch temperature data for specific coordinates and time intervals.
- **High Performance:** Optimized with asynchronous I/O operations and in-memory caching.
- **Docker Support:** Easily deployable with Docker and Docker Compose.

## Installation

### Prerequisites

- Python 3.12
- Poetry
- Docker (optional)
- Docker Compose (optional)

### Local Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/meteorological-api.git
   cd meteorological-api
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Run the application:**

   ```bash
   poetry run uvicorn meteorological_api.main:app --reload
   ```

4. **Access the API:**

   The API will be available at [http://localhost:8000](http://localhost:8000).

### Docker Installation

1. **Build the Docker image:**

   ```bash
   docker-compose build
   ```

2. **Run the application using Docker Compose:**

   ```bash
   docker-compose up -d
   ```

3. **Access the API:**

   The API will be available at [http://localhost:8000](http://localhost:8000).

## Usage

### Endpoint: GET /getForecast

Retrieve temperature data based on coordinates and time intervals.

**Parameters:**

- `from_ts` (int): Start timestamp (Unix format).
- `to_ts` (int): End timestamp (Unix format).
- `lat` (float): Latitude.
- `lon` (float): Longitude.

**Example Request:**

```bash
curl "http://localhost:8000/getForecast?from_ts=1688504400&to_ts=1688504400&lat=50.0&lon=20.0"
```

**Example Response:**

```json
{
  "1688504400": {
    "temp": 287.3999938964844
  }
}
```

## Project Structure

```plaintext
.
├── files                    # Binary data files
│   ├── 1688497200.wgf4
│   ├── 1688500800.wgf4
│   └── 1688504400.wgf4
├── meteorological_api       # Application source code
│   ├── __init__.py
│   ├── main.py              # Entry point for FastAPI application
│   ├── services             # Service layer for reading binary files
│   │   ├── file_reader.py
│   │   ├── __init__.py
│   └── tests                # Test cases for the application
│       ├── test_api.py
│       ├── test_file_reader.py
├── poetry.lock              # Poetry lock file for dependencies
├── pyproject.toml           # Project configuration
├── Dockerfile               # Dockerfile for building the Docker image
├── docker-compose.yml       # Docker Compose configuration
└── README.md                # Project documentation
```

## License

This project is licensed under the MIT License.

## Pulling the Docker Image from Docker Hub

If you prefer to use the pre-built Docker image, you can pull it directly from Docker Hub.

### Command:

```bash
docker pull pavlovva/meteorological-api:latest
```

After pulling the image, you can run it with the following command:

```bash
docker run -d -p 8000:8000 pavlovva/meteorological-api:latest
```

The API will be available at [http://localhost:8000](http://localhost:8000).