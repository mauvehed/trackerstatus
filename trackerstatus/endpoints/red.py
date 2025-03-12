from typing import Any, Dict

from trackerstatus.core import APIClient
from trackerstatus.endpoints.base import BaseTrackerEndpoint


class REDEndpoint(BaseTrackerEndpoint):
    """Endpoint for retrieving Redacted specific status information."""

    def __init__(self, client: APIClient) -> None:
        super().__init__(client)
        self._tracker_prefix = "red"

    def get_status(self) -> Dict[str, Any]:
        """
        Get the current status of all RED services.

        Returns:
            dict: Status information for all RED services
        """
        return self.client.get("api/red/status")

    def get_all(self) -> Dict[str, Any]:
        """
        Get combined data for all RED services.

        Returns:
            dict: Combined information for all RED services
        """
        return self.client.get("api/red/all")
