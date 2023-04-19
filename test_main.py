import pytest
from fastapi.testclient import TestClient


from main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


def test_root_endpoint_connection_with_root(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_root_endpoint_only_get(client):
    resp = client.post("/")
    assert resp.status_code == 405
    assert resp.json() == {"detail": "Method Not Allowed"}
