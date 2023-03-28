from unittest.mock import patch, MagicMock

from starlette.testclient import TestClient

import main


def test_my_func():
    with TestClient(main.app) as client:
        test_mock = MagicMock(return_value={"message": "Hello John"})

        with patch('main.say_hello', test_mock):
            response = client.get("/hello/John")

        assert response.status_code == 200
        assert response.json() == {"message": "Hello John"}
