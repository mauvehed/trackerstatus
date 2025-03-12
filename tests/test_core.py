import time
from unittest.mock import MagicMock

import pytest
import requests

from trackerstatus.core import APIClient


def test_api_client_initialization() -> None:
    """Test APIClient initialization with default and custom URLs."""
    client = APIClient()
    assert client.base_url == "https://trackerstatus.info"

    custom_url = "https://btn.trackerstatus.info"
    client = APIClient(base_url=custom_url)
    assert client.base_url == custom_url


def test_rate_limiting() -> None:
    """Test that rate limiting is enforced."""
    client = APIClient()
    client.last_request_time = time.time()

    start_time = time.time()
    client._enforce_rate_limit()
    elapsed = time.time() - start_time

    assert elapsed >= 60, "Rate limiting should enforce a 60-second delay"


def test_get_request_success(requests_mock: MagicMock) -> None:
    """Test successful GET request."""
    client = APIClient()
    mock_data = {"status": "ok"}
    requests_mock.get("https://trackerstatus.info/api/test", json=mock_data)

    response = client.get("api/test")
    assert response == mock_data


def test_get_request_http_error(requests_mock: MagicMock) -> None:
    """Test HTTP error handling."""
    client = APIClient()
    requests_mock.get("https://trackerstatus.info/api/test", status_code=404)

    with pytest.raises(requests.HTTPError):
        client.get("api/test")


def test_get_request_invalid_json(requests_mock: MagicMock) -> None:
    """Test invalid JSON response handling."""
    client = APIClient()
    requests_mock.get("https://trackerstatus.info/api/test", text="invalid json")

    with pytest.raises(ValueError):
        client.get("api/test")


def test_get_request_non_dict_response(requests_mock: MagicMock) -> None:
    """Test response that is valid JSON but not a dictionary."""
    client = APIClient()
    requests_mock.get("https://trackerstatus.info/api/test", json=["not", "a", "dict"])

    with pytest.raises(TypeError, match="API response must be a dictionary"):
        client.get("api/test")


def test_get_request_general_error(requests_mock: MagicMock) -> None:
    """Test general error handling."""
    client = APIClient()
    requests_mock.get(
        "https://trackerstatus.info/api/test", exc=Exception("test error")
    )

    with pytest.raises(Exception, match="An error occurred: test error"):
        client.get("api/test")


def test_url_construction() -> None:
    """Test URL construction with different input formats."""
    client = APIClient()

    # Test with and without leading slash
    assert client._construct_url("api/test") == client._construct_url("/api/test")

    # Test with full URL
    assert client._construct_url(
        "https://trackerstatus.info/api/test"
    ) == client._construct_url("api/test")
