from typing import Any, Dict

import pytest
from requests_mock import Mocker

from trackerstatus.core import APIClient
from trackerstatus.endpoints.status import StatusEndpoint


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to create an APIClient instance.

    Returns:
        APIClient: An instance of the APIClient.
    """
    return APIClient(base_url="https://trackerstatus.info")


@pytest.fixture
def status_endpoint(api_client: APIClient) -> StatusEndpoint:
    """
    Fixture to create a StatusEndpoint instance.

    Args:
        api_client (APIClient): An instance of the APIClient.

    Returns:
        StatusEndpoint: An instance of the StatusEndpoint.
    """
    return StatusEndpoint(client=api_client)


def test_get_tracker_statuses(
    status_endpoint: StatusEndpoint, requests_mock: Mocker
) -> None:
    """
    Tests the get_tracker_statuses method of the StatusEndpoint.

    Args:
        status_endpoint (StatusEndpoint): An instance of the StatusEndpoint.
    """
    mock_data = {"ar": 1, "btn": 1, "ggn": 1, "ptp": 1, "red": 1, "ops": 1}
    requests_mock.get("https://trackerstatus.info/api/list", json=mock_data)

    response = status_endpoint.get_tracker_statuses()
    assert isinstance(response, dict)
    assert "ar" in response
    assert isinstance(response["ar"], dict)
    assert "status_code" in response["ar"]
    assert "status_message" in response["ar"]


def test_get_status_alias(
    status_endpoint: StatusEndpoint, requests_mock: Mocker
) -> None:
    """
    Test that get_status is properly aliased to get_tracker_statuses.

    Args:
        status_endpoint (StatusEndpoint): An instance of the StatusEndpoint.
        requests_mock (Mocker): Request mocker for simulating API calls.
    """
    mock_data = {"ar": 1, "btn": 1}
    requests_mock.get("https://trackerstatus.info/api/list", json=mock_data)

    status_response = status_endpoint.get_status()
    tracker_response = status_endpoint.get_tracker_statuses()
    assert status_response == tracker_response
