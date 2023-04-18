import unittest
from unittest.mock import patch, MagicMock, Mock
import requests
from starlette.testclient import TestClient
from jsonPlaceHolderFetcher import jsonPlaceHolderFetcher
import main


def test_api_call():
    real = jsonPlaceHolderFetcher()
    real.end_point_status_code = MagicMock(name="connectToEndpoint")
    real.end_point_status_code.return_value.status_code = 200

    with patch("requests.get", real):
        data = real.end_point_status_code("/").status_code

    assert data == 200
