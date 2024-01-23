#!/usr/bin/env python

from fastapi.testclient import TestClient

from bng36_wgs84_conversion.main import app

client = TestClient(app)


def test_bng_to_wgs84_conversion():
    response = client.post(
        "/convert/bng_to_wgs84", json={"easting": 530000, "northing": 180000}
    )
    assert response.status_code == 200

    data = response.json()

    assert "latitude" in data
    assert "longitude" in data

    assert data == {"latitude": 51.50399082763378, "longitude": -0.12835394047946933}


def test_wgs84_to_bng_conversion():
    response = client.post(
        "/convert/wgs84_to_bng", json={"latitude": 51.5074, "longitude": -0.1278}
    )
    assert response.status_code == 200

    data = response.json()

    assert "easting" in data
    assert "northing" in data

    assert data == {"easting": 530028.7469491748, "northing": 180380.09425125353}
