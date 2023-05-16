import pytest
from fastapi.testclient import TestClient
import jsonPlaceHolderFetcher

from main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


def test_root_endpoint_connection_with_root(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_root_endpoint_post(client):
    resp = client.post("/")
    assert resp.status_code == 405
    assert resp.json() == {"detail": "Method Not Allowed"}


def test_endpoint_mainpage(client):
    resp = client.get("/mainpage")
    assert resp.status_code == 200


def test_endpoint_users(client):
    resp = client.get("/users")
    assert resp.status_code == 200


def test_endpoint_posts(client):
    resp = client.get("/posts")
    assert resp.status_code == 200
