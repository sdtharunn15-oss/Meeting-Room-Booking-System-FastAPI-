from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Meeting Room Booking API"
    }


def test_get_employees():

    response = client.get("/employees/")

    assert response.status_code == 200


def test_get_rooms():

    response = client.get("/rooms/")

    assert response.status_code == 200


def test_get_bookings():

    response = client.get("/bookings/")

    assert response.status_code == 200