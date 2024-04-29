from fastapi.testclient import TestClient
from main import app
from db import TruckQueries

client = TestClient(app)

class EmptyTruckQueries:
    def get_trucks(self):
        return []

class CreateTruckQueries:
    def create_truck(self,truck):
        result = {
            "id": 1010,
            "owner": {
                "id": 8888,
                "first": "Owner",
                "last": "Truck",
                "avatar": "avatar",
                "email": "email@email.com",
                "username": "owner_truck"
            },
        }
        result.update(truck)
        return result 


def test_get_all_trucks():
     # Arrange
    app.dependency_overrides[TruckQueries] = EmptyTruckQueries

    response = client.get("/api/trucks")

    # Act 
    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == {"trucks":[]}


def test_create_trucks():
     # Arrange
    app.dependency_overrides[TruckQueries] = CreateTruckQueries

    json = {
        "name": "Plink",
        "website": "http://plinko.example.com",
        "category": "American",
        "vegetarian_friendly": True,
        "owner_id": 2
    }

    expected = {
        "id": 1010,
        "name": "Plink",
        "website": "http://plinko.example.com",
        "category": "American",
        "vegetarian_friendly": True,
        "owner": {
            "id": 8888,
            "first": "Owner",
            "last": "Truck",
            "avatar": "avatar",
            "email": "email@email.com",
            "username": "owner_truck"
        },
    }

    # Act 
    response = client.post("/api/trucks", json=json)

    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == expected

def test_init():
    assert 1 == 1