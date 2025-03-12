from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class PTPEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving PassThePopcorn specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "ptp"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all PTP services.

        Returns:
            dict: Status information for all PTP services
        """
        return self.client.get("api/ptp/status")

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all PTP services.

        Returns:
            dict: Combined information for all PTP services
        """
        return self.client.get("api/ptp/all")
