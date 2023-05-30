"""mocktests for the project, mocking jsonplaceholder"""

from unittest.mock import patch, MagicMock
from jsonPlaceHolderFetcher import jsonPlaceHolderFetcher


def test_api_call():
    """tests connection with jsonplaceholder"""
    real = jsonPlaceHolderFetcher()
    real.end_point_status_code = MagicMock(name="connectToEndpoint")
    real.end_point_status_code.return_value.status_code = 200

    with patch("requests.get", real):
        data = real.end_point_status_code("/").status_code

    assert data == 200
