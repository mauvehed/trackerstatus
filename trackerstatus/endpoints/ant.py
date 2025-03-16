from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class ANTEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving Anthelion specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "ant"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all ANT services.

        Returns:
            dict: Status information for all ANT services
        """
        return self.client.get(
            self._get_endpoint("status"), tracker_prefix=self._tracker_prefix
        )

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all ANT services.

        Returns:
            dict: Combined information for all ANT services
        """
        return self.client.get(
            self._get_endpoint("all"), tracker_prefix=self._tracker_prefix
        )
