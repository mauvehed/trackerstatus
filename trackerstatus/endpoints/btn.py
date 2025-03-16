from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class BTNEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving BTN (BroadcastTheNet) specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "btn"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all BTN services.

        Returns:
            dict: Status information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_latency(self) -> Dict[str, Any]:
        """
        Get the current latency of all BTN services.

        Returns:
            dict: Latency information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("latency"), tracker_prefix=self._tracker_prefix
        )

    def get_uptime(self) -> Dict[str, Any]:
        """
        Get the current uptime of all BTN services.

        Returns:
            dict: Uptime information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("uptime"), tracker_prefix=self._tracker_prefix
        )

    def get_records(self) -> Dict[str, Any]:
        """
        Get the best recorded uptime of all BTN services.

        Returns:
            dict: Record information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("records"), tracker_prefix=self._tracker_prefix
        )

    def get_downtime(self) -> Dict[str, Any]:
        """
        Get the current downtime of all BTN services.

        Returns:
            dict: Downtime information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("downtime"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all BTN services.
        Includes status, latency, uptime, records, and downtime.

        Returns:
            dict: Combined information for all BTN services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )
