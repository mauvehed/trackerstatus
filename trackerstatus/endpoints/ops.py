from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class OPSEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving Orpheus specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "ops"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all OPS services.

        Returns:
            dict: Status information for all OPS services
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all OPS services.

        Returns:
            dict: Combined information for all OPS services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )
