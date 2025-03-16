from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class GGNEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving GazelleGames specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "ggn"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all GGN services.

        Returns:
            dict: Status information for all GGN services
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all GGN services.

        Returns:
            dict: Combined information for all GGN services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )
