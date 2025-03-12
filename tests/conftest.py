from typing import Any, Dict

import pytest

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class TestTrackerEndpoint(BaseTrackerEndpoint):
    """Test implementation of BaseTrackerEndpoint."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "test"


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to create an APIClient instance.

    Returns:
        APIClient: An instance of the APIClient.
    """
    return APIClient(base_url="https://trackerstatus.info")


@pytest.fixture
def mock_response() -> Dict[str, Any]:
    """
    Fixture to provide a mock response for testing.

    Returns:
        dict: A mock response dictionary
    """
    return {
        "status_code": {
            "Description": "All systems operational",
            "Details": {
                "Website": "1",
                "TrackerHTTP": "1",
                "TrackerHTTPS": "1",
                "IRCServer": "1",
                "IRCTorrentAnnouncer": "1",
                "IRCUserIdentifier": "1",
            },
        }
    }


@pytest.fixture
def test_endpoint(api_client: APIClient) -> BaseTrackerEndpoint:
    """
    Fixture to create a test endpoint instance.

    Args:
        api_client: APIClient fixture

    Returns:
        BaseTrackerEndpoint: A test endpoint instance
    """
    return TestTrackerEndpoint(api_client)
