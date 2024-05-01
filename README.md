# BNG36 <--> WGS84 Coordinate Conversion API

This is a simple FastAPI application for converting coordinates between the British National Grid (BNG, OSGB36) system and the WGS84 coordinate system. [Pyproj](https://pypi.org/project/pyproj) is used for coordinate conversions. **This is an example and should not be used in Production**

## Features

- Convert from BNG (OSGB36) to WGS84 coordinates.
- Convert from WGS84 to BNG (OSGB36) coordinates.

## Installation

To run this application, you will need Python installed on your system. The application uses FastAPI and pyproj for coordinate conversions, and [Poetry](https://python-poetry.org) to manage the project.

1. Clone this repository:

   ```bash
   git clone https://github.com/face0b1101/bng36-wgs84-conversion
   ```

2. Navigate to the cloned directory:

   ```bash
   cd bng36-wgs84-conversion
   ```

3. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

To start the application, you can use Poetry to run the Uvicorn server:

```bash
poetry run uvicorn bng36_wgs84_conversion.main:app --reload
```

The application will start on `http://127.0.0.1:8000`. You can access the API documentation and try out the API by navigating to `http://127.0.0.1:8000/docs`.

There is also a notebook, `test.ipynb`, that you can use to test the API.

### Docker

You can also use Docker to build and run the application.

Build the Docker image and run it with the following environment variables.

```sh
# docker build -f Dockerfile -t face0b1101/hmrc-chatbot-rag-demo .
DOCKER_BUILDKIT=1 docker build -f Dockerfile --target runtime -t face0b1101/bng36-wgs84-conversion:0.1 .

# or...
docker compose build
```

### API Endpoints

- `POST /convert/bng_to_wgs84`: Converts BNG (OSGB36) coordinates to WGS84 coordinates.
  - Input: JSON with `easting` and `northing` fields.
  - Output: JSON with `latitude` and `longitude` fields.

- `POST /convert/wgs84_to_bng`: Converts WGS84 coordinates to BNG (OSGB36) coordinates.
  - Input: JSON with `latitude` and `longitude` fields.
  - Output: JSON with `easting` and `northing` fields.

## Example

```json
// BNG to WGS84
POST /convert/bng_to_wgs84
{
  "easting": 530000,
  "northing": 180000
}

// WGS84 to BNG
POST /convert/wgs84_to_bng
{
  "latitude": 51.5074,
  "longitude": -0.1278
}
```
