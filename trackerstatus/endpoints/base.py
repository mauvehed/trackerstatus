from enum import IntEnum
from typing import Any, Dict

from trackerstatus.core import APIClient


class TrackerStatus(IntEnum):
    """Enumeration of possible tracker statuses."""

    OFFLINE = 0
    ONLINE = 1
    UNSTABLE = 2


class BaseTrackerEndpoint:
    """Base class for all tracker-specific endpoints."""

    def __init__(self, client: APIClient):
        """
        Initialize the tracker endpoint.

        Args:
            client (APIClient): Instance of the API client
        """
        self.client = client
        self._tracker_prefix = ""  # To be set by subclasses (e.g., "btn", "ar", etc.)

    def _get_endpoint(self, endpoint: str) -> str:
        """
        Construct the full endpoint path.

        Args:
            endpoint (str): The endpoint name

        Returns:
            str: The full endpoint path
        """
        return endpoint

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all services.

        Returns:
            dict: Status information including tweet data
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_latency(self) -> Dict[str, Any]:
        """
        Get the current response latency of all services.

        Returns:
            dict: Latency information for all services
        """
        return self.client.get(
            self._get_endpoint("latency"), tracker_prefix=self._tracker_prefix
        )

    def get_uptime(self) -> Dict[str, Any]:
        """
        Get the current uptime of all services in minutes.

        Returns:
            dict: Uptime information for all services
        """
        return self.client.get(
            self._get_endpoint("uptime"), tracker_prefix=self._tracker_prefix
        )

    def get_records(self) -> Dict[str, Any]:
        """
        Get the best recorded uptime of all services in minutes.

        Returns:
            dict: Record information for all services
        """
        return self.client.get(
            self._get_endpoint("records"), tracker_prefix=self._tracker_prefix
        )

    def get_downtime(self) -> Dict[str, Any]:
        """
        Get the current downtime of all services.

        Returns:
            dict: Downtime information for all services
        """
        return self.client.get(
            self._get_endpoint("downtime"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all services.
        Includes status, latency, uptime, records, and downtime.

        Returns:
            dict: Combined information for all services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )

    @staticmethod
    def interpret_status(status: int) -> str:
        """
        Convert numeric status to human-readable string.

        Args:
            status (int): Numeric status code

        Returns:
            str: Human-readable status
        """
        try:
            return {
                TrackerStatus.OFFLINE: "Offline - no response over the past 3 minutes",
                TrackerStatus.ONLINE: "Online - perfect response over the past 3 minutes",
                TrackerStatus.UNSTABLE: "Unstable - intermittent responses over the past 3 minutes",
            }[TrackerStatus(status)]
        except ValueError:
            return f"Unknown status code: {status}"
