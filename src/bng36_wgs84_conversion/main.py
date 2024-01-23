#!/usr/bin/env python

import pyproj
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BNGCoordinates(BaseModel):
    easting: float
    northing: float


class WGS84Coordinates(BaseModel):
    latitude: float
    longitude: float


def bng_to_wgs84(easting: float, northing: float) -> tuple:
    """
    Convert British National Grid (BNG) coordinates to WGS84 (latitude, longitude).

    Args:
        easting (float): The easting coordinate in BNG.
        northing (float): The northing coordinate in BNG.

    Returns:
        tuple: A tuple containing the latitude and longitude in WGS84.
    """
    bng = pyproj.CRS("EPSG:27700")
    wgs84 = pyproj.CRS("EPSG:4326")

    transformer = pyproj.Transformer.from_crs(bng, wgs84, always_xy=True)
    lon, lat = transformer.transform(easting, northing)

    return lat, lon


def wgs84_to_bng(lat: float, lon: float) -> tuple:
    """
    Convert WGS84 coordinates to British National Grid (BNG) using pyproj library.

    Args:
        lat (float): The latitude in WGS84 format.
        lon (float): The longitude in WGS84 format.

    Returns:
        tuple: A tuple containing the easting and northing in BNG format.
    """

    wgs84 = pyproj.CRS("EPSG:4326")
    bng = pyproj.CRS("EPSG:27700")

    transformer = pyproj.Transformer.from_crs(wgs84, bng, always_xy=True)
    easting, northing = transformer.transform(lon, lat)

    return easting, northing


@app.post("/convert/bng_to_wgs84")
async def convert_bng_to_wgs84(coordinates: BNGCoordinates) -> dict:
    """
    Python FastAPI endpoint that takes BNG (Eastings, Northings) coordinates
    and returns WGS84 coordinates.

    Args:
        coordinates (BNGCoordinates): The BNGCoordinates to convert.

    Returns:
        dict: a dictionary containing the latitude and longitude WGS84 coordinates.
    """

    lat, lon = bng_to_wgs84(coordinates.easting, coordinates.northing)

    return {"latitude": lat, "longitude": lon}


@app.post("/convert/wgs84_to_bng")
async def convert_wgs84_to_bng(coordinates: WGS84Coordinates) -> dict:
    """
    Python FastAPI endpoint that takes WGS84 coordinates and returns
    British National Grid (BNG) coordinates.

    Args:
        coordinates (WGS84Coordinates): The WGS84 coordinates to convert.

    Returns:
        dict: A dictionary containing the easting and northing BNG coordinates.
    """

    easting, northing = wgs84_to_bng(coordinates.latitude, coordinates.longitude)

    return {"easting": easting, "northing": northing}
