from typing import Any, Tuple

import pytest
from requests_mock import Mocker

from trackerstatus.core import APIClient
from trackerstatus.endpoints.ar import AREndpoint
from trackerstatus.endpoints.base import BaseTrackerEndpoint
from trackerstatus.endpoints.btn import BTNEndpoint
from trackerstatus.endpoints.ggn import GGNEndpoint
from trackerstatus.endpoints.ops import OPSEndpoint
from trackerstatus.endpoints.ptp import PTPEndpoint
from trackerstatus.endpoints.red import REDEndpoint


@pytest.fixture(
    params=[
        (AREndpoint, "ar"),
        (BTNEndpoint, "btn"),
        (GGNEndpoint, "ggn"),
        (PTPEndpoint, "ptp"),
        (REDEndpoint, "red"),
        (OPSEndpoint, "ops"),
    ]
)
def tracker_endpoint(
    request: Any, api_client: APIClient
) -> Tuple[BaseTrackerEndpoint, str]:
    """
    Parametrized fixture that creates instances of all tracker endpoints.

    Args:
        request: Pytest request object containing the endpoint class and prefix
        api_client: APIClient fixture

    Returns:
        tuple: (endpoint instance, tracker prefix)
    """
    endpoint_class, prefix = request.param
    return endpoint_class(api_client), prefix


def test_tracker_prefix(tracker_endpoint: Tuple[BaseTrackerEndpoint, str]) -> None:
    """Test that each tracker endpoint has the correct prefix."""
    endpoint, expected_prefix = tracker_endpoint
    # pylint: disable=protected-access
    assert endpoint._tracker_prefix == expected_prefix


@pytest.mark.parametrize(
    "method_name",
    [
        "get_status",
        "get_latency",
        "get_uptime",
        "get_records",
        "get_downtime",
        "get_all",
    ],
)
def test_endpoint_methods(
    tracker_endpoint: Tuple[BaseTrackerEndpoint, str],
    method_name: str,
    requests_mock: Mocker,
    mock_response: dict,
) -> None:
    """Test all standard methods for each tracker endpoint."""
    endpoint, prefix = tracker_endpoint
    endpoint_name = method_name.split("_")[1]
    url = f"https://{prefix}.trackerstatus.info/api/{endpoint_name}"

    # Create appropriate mock response based on the endpoint
    if method_name == "get_all":
        mock_data = {
            "status": mock_response,
            "latency": {"Website": 100},
            "uptime": {"Website": 1440},
            "records": {"Website": 14400},
            "downtime": {"Website": 0},
        }
    else:
        mock_data = mock_response

    requests_mock.get(url, json=mock_data)
    response = getattr(endpoint, method_name)()
    assert response == mock_data


def test_status_response(
    tracker_endpoint: Tuple[BaseTrackerEndpoint, str], requests_mock: Mocker
) -> None:
    """Test the status endpoint response format."""
    endpoint, prefix = tracker_endpoint
    url = f"https://{prefix}.trackerstatus.info/api/status"

    mock_data = {
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

    requests_mock.get(url, json=mock_data)
    response = endpoint.get_status()
    assert response == mock_data


def test_all_response(
    tracker_endpoint: Tuple[BaseTrackerEndpoint, str], requests_mock: Mocker
) -> None:
    """Test the all endpoint response format."""
    endpoint, prefix = tracker_endpoint
    url = f"https://{prefix}.trackerstatus.info/api/all"

    mock_data = {
        "status": {
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
        },
        "latency": {
            "Website": 100,
            "TrackerHTTP": 100,
            "TrackerHTTPS": 100,
            "IRCServer": 100,
            "IRCTorrentAnnouncer": 100,
            "IRCUserIdentifier": 100,
        },
        "uptime": {
            "Website": 1440,
            "TrackerHTTP": 1440,
            "TrackerHTTPS": 1440,
            "IRCServer": 1440,
            "IRCTorrentAnnouncer": 1440,
            "IRCUserIdentifier": 1440,
        },
        "records": {
            "Website": 14400,
            "TrackerHTTP": 14400,
            "TrackerHTTPS": 14400,
            "IRCServer": 14400,
            "IRCTorrentAnnouncer": 14400,
            "IRCUserIdentifier": 14400,
        },
        "downtime": {
            "Website": 0,
            "TrackerHTTP": 0,
            "TrackerHTTPS": 0,
            "IRCServer": 0,
            "IRCTorrentAnnouncer": 0,
            "IRCUserIdentifier": 0,
        },
    }

    requests_mock.get(url, json=mock_data)
    response = endpoint.get_all()
    assert response == mock_data
