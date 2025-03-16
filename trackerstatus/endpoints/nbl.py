from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class NBLEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving Nebulance specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "nbl"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all NBL services.

        Returns:
            dict: Status information for all NBL services
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all NBL services.

        Returns:
            dict: Combined information for all NBL services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )
