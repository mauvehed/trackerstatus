from typing import Dict

import pytest
from requests_mock import Mocker

from trackerstatus.endpoints.base import BaseTrackerEndpoint, TrackerStatus


def test_tracker_status_values() -> None:
    """Test TrackerStatus enum values."""
    # pylint: disable=comparison-with-callable
    assert TrackerStatus.OFFLINE == 0
    assert TrackerStatus.ONLINE == 1
    assert TrackerStatus.UNSTABLE == 2


def test_interpret_status_valid(test_endpoint: BaseTrackerEndpoint) -> None:
    """Test status code interpretation with valid codes."""
    assert "Offline" in test_endpoint.interpret_status(TrackerStatus.OFFLINE)
    assert "Online" in test_endpoint.interpret_status(TrackerStatus.ONLINE)
    assert "Unstable" in test_endpoint.interpret_status(TrackerStatus.UNSTABLE)


def test_interpret_status_invalid(test_endpoint: BaseTrackerEndpoint) -> None:
    """Test status code interpretation with invalid code."""
    assert "Unknown status code: 999" == test_endpoint.interpret_status(999)


def test_get_endpoint_with_prefix(test_endpoint: BaseTrackerEndpoint) -> None:
    """Test endpoint URL construction with prefix."""
    # pylint: disable=protected-access
    assert test_endpoint._get_endpoint("status") == "status"


def test_get_endpoint_without_prefix(test_endpoint: BaseTrackerEndpoint) -> None:
    """Test endpoint URL construction without prefix."""
    # pylint: disable=protected-access
    test_endpoint._tracker_prefix = ""
    # pylint: disable=protected-access
    assert test_endpoint._get_endpoint("status") == "status"


def test_required_methods_exist(test_endpoint: BaseTrackerEndpoint) -> None:
    """Test that all required endpoint methods exist."""
    required_methods = [
        "get_status",
        "get_latency",
        "get_uptime",
        "get_records",
        "get_downtime",
        "get_all",
    ]
    for method in required_methods:
        assert hasattr(test_endpoint, method)
        assert callable(getattr(test_endpoint, method))


def test_base_get_status(
    test_endpoint: BaseTrackerEndpoint, requests_mock: Mocker
) -> None:
    """Test the base get_status method."""
    mock_data = {
        "status_code": {
            "Description": "All systems operational",
            "Details": {"Website": "1"},
        }
    }
    requests_mock.get("https://test.trackerstatus.info/api/status", json=mock_data)
    response = test_endpoint.get_status()
    assert response == mock_data


def test_base_get_all(
    test_endpoint: BaseTrackerEndpoint, requests_mock: Mocker
) -> None:
    """Test the base get_all method."""
    mock_data = {
        "status": {
            "status_code": {
                "Description": "All systems operational",
                "Details": {"Website": "1"},
            }
        },
        "latency": {"Website": 100},
        "uptime": {"Website": 1440},
        "records": {"Website": 14400},
        "downtime": {"Website": 0},
    }
    requests_mock.get("https://test.trackerstatus.info/api/all", json=mock_data)
    response = test_endpoint.get_all()
    assert response == mock_data
